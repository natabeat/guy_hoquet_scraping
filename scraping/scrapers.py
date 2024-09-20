from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config.settings import CHROMEDRIVER_PATH, BASE_URL


def scrape_addresses(names):
    addresses = []

    # Lancer le navigateur Chrome
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    driver.get(BASE_URL)

    # Accepter les cookies
    driver.find_element_by_id("didomi-notice-agree-button").click()

    for name in names:
        # Rechercher l'entreprise
        searchbar = driver.find_element_by_id("input_search")
        searchbar.send_keys(name)
        searchbar.send_keys(Keys.ENTER)

        # Sélectionner le premier résultat
        driver.find_element_by_class_name("ResultBloc__link__content").click()

        # Extraire l'adresse
        address = driver.find_element_by_id("adressHover").find_elements_by_class_name("adressText")
        full_address = " ".join([element.get_attribute("textContent") for element in address])
        addresses.append(full_address.strip())

    # Fermer le navigateur
    driver.quit()

    return addresses
