from scraping.scrapers import scrape_addresses
from scraping.map_generator import generate_map
from config.settings import NAMES


def main():
    # Scraper les adresses
    addresses = scrape_addresses(NAMES)
    print(f"Adresses trouvées : {addresses}")

    # Générer la carte
    generate_map(NAMES, addresses)


if __name__ == "__main__":
    main()
