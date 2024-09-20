import requests
from config.settings import HEADERS

def scrape_website(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to scrape {url}")
