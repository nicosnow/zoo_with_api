# Animal Website Generator

This project generates a website with information about animals. It fetches data from an API and uses it to create an HTML file.
with a funny touch if the animal doesn't exist :)

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your API key:
   ```dotenv
   API_KEY = 'your_api_key_here'
   ```

## Usage

1. Run the `animals_web_generator.py` script:
   ```sh
   python animals_web_generator.py
   ```

2. Enter the name of an animal when prompted.

3. The script will generate an `animals.html` file with the animal information.

## Files

- `animals_web_generator.py`: Main script to generate the website.
- `data_fetcher.py`: Module to fetch animal data from the API.
- `requirements.txt`: List of required Python packages.
- `.env`: File to store environment variables (API key).

## Dependencies

- `requests`
- `python-dotenv`

## License

This project is licensed under the MIT License.