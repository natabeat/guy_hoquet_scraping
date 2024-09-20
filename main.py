from scraping.scrapers import scrape_addresses, scrape_guy_hoquet
from scraping.map_generator import generate_map, generate_map_guy_hoquet
from config.settings import NAMES


def main():
    # Scraper les adresses
    #addresses = scrape_addresses(NAMES)
    #print(f"Adresses trouvées : {addresses}")
    announces = scrape_guy_hoquet()

    # Générer la carte
    #generate_map(NAMES, addresses)

if __name__ == "__main__":
    main()
