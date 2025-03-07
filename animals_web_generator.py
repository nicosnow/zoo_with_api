import json
import requests

def load_data(api_url, headers):
    """Fetches data from an API"""
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

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

# Ask the user for the animal name
animal_name = input("Enter a name of an animal: ")
api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
headers = {'X-Api-Key': 'DvIoMAmPdJJzgK+zTp6uMQ==u6mcPpCQgdZY7LeU'}

animals_data = load_data(api_url, headers)

if not animals_data:
    all_animals_info = """
    <li class='cards__item'>
        <div class='card__title'>I'm sorry, that's an interesting name, but that animal doesn't exist or is not registered in our database... yet?</div>
        <img src='fake_animal.jpg' alt='Fake Animal' style='width:50%;height:auto;'/>
    </li>
    """
else:
    all_animals_info = ""
    for animal in animals_data:
        all_animals_info += get_animal_info(animal) + "\n"

generate_html(all_animals_info, 'animals_template.html', 'animals.html')

print("Website was successfully generated to the file animals.html.")