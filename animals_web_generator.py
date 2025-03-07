import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_info(animal):
    """Returns the specified fields of an animal as a formatted string if they exist"""
    info = []
    if 'name' in animal:
        info.append(f"<li class='cards__item'><div class='card__title'>{animal['name']}</div>")
    if 'diet' in animal['characteristics'] or 'locations' in animal or 'type' in animal['characteristics']:
        info.append("<p class='card__text'>")
        if 'diet' in animal['characteristics']:
            info.append(f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>")
        if 'locations' in animal and animal['locations']:
            info.append(f"<strong>Location:</strong> {' and '.join(animal['locations'])}<br/>")
        if 'type' in animal['characteristics']:
            info.append(f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>")
        info.append("</p></li>")
    return "\n".join(info)


def generate_html(animals_info, template_path, output_path):
    """Generates an HTML file with the animals' information"""
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, "w") as output_file:
        output_file.write(updated_content)


animals_data = load_data('animals_data.json')

all_animals_info = ""
for animal in animals_data:
    all_animals_info += get_animal_info(animal) + "\n"

generate_html(all_animals_info, 'animals_template.html', 'animals.html')