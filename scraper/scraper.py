# scraper/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_data_gov():
    url = "https://www.data.gov"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    datasets = soup.find_all('a', class_='dataset-heading')
    for dataset in datasets:
        title = dataset.get_text().strip()
        link = dataset['href']
        description = ""  # Scrape descriptions if necessary

        # Process data without saving to the database
        # For example, you could log it or send it to another service
        print(f"Title: {title}, Link: {link}, Description: {description}")

def scrape_worldbank():
    url = "https://data.worldbank.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    datasets = soup.find_all('a', class_='indicators-list-item')
    for dataset in datasets:
        title = dataset.get_text().strip()
        link = dataset['href']
        description = ""  # Scrape descriptions if necessary

        # Process data without saving to the database
        print(f"Title: {title}, Link: {link}, Description: {description}")

