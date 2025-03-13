import os
import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please set it in the .env file.")

def fetch_animal_data(name):
    """Fetch animal data from Ninja API."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP failures (4xx, 5xx)
        data = response.json()

        if not data:
            print(f"No data found for '{name}'. Please try another animal.")
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None