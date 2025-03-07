import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes

    return response.json()