from functions.scrapers import scrape_website
from functions.parsers import parse_data
from utils.helpers import save_to_csv

def main():
    url = "https://www.guy-hoquet.com"
    raw_data = scrape_website(url)
    parsed_data = parse_data(raw_data)
    save_to_csv(parsed_data, "data/results.csv")

if __name__ == "__main__":
    main()
