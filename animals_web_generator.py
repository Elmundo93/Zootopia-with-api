
from dataFetcha import fetch_animal_data

def generate_animal_cards(animals):
    cards_html = ""
    for animal in animals:
        info = []
        if "name" in animal:
            info.append(f"<p><strong>Name:</strong> {animal['name']}</p>")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            info.append(f"<p><strong>Diet:</strong> {animal['characteristics']['diet']}</p>")
        if "locations" in animal and animal["locations"]:
            info.append(f"<p><strong>Location:</strong> {animal['locations'][0]}</p>")
        if "characteristics" in animal and "type" in animal["characteristics"]:
            info.append(f"<p><strong>Type:</strong> {animal['characteristics']['type']}</p>")

        if info:
            cards_html += f"<li class='cards__item'>{''.join(info)}</li>\n"
    return cards_html


def generate_final_html(animal_name, html_template_file, output_file):
    animals = fetch_animal_data(animal_name)  # Use the imported function

    if animals is None:
        print("Skipping HTML generation due to missing data.")
        return

    try:
        with open(html_template_file, "r", encoding="utf-8") as file:
            html_template = file.read()
    except FileNotFoundError:
        print(f"Error: Template file '{html_template_file}' not found.")
        return

    animals_html = generate_animal_cards(animals)
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(final_html)
        print(f"Final HTML generated successfully: {output_file}")
    except IOError:
        print(f"Error writing to output file '{output_file}'. Please check permissions.")


if __name__ == "__main__":
    print("Welcome to the Animal Info Generator!")

    while True:
        animal_name = input("Enter an animal name (or type 'exit' to quit): ").strip().lower()

        if animal_name == "exit":
            print("Exiting program. Have a great day!")
            break

        if not animal_name:
            print("Invalid input. Please enter a valid animal name.")
            continue

        generate_final_html(animal_name, "animals_template.html", "animals_repository.html")