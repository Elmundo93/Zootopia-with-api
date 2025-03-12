import json


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


def generate_final_html(json_file, html_template_file, output_file):
    with open(json_file, "r", encoding="utf-8") as file:
        animals = json.load(file)

    with open(html_template_file, "r", encoding="utf-8") as file:
        html_template = file.read()

    animals_html = generate_animal_cards(animals)

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)


    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Final HTML generated successfully.")


# Example usage:
generate_final_html("animals_data.json", "animals_template.html", "animals_repository.html")