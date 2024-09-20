from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importer Service
from selenium.webdriver.common.by import By  # Importer By
from selenium.webdriver.common.keys import Keys
from config.settings import CHROMEDRIVER_PATH, BASE_URL


def scrape_addresses(names):
    addresses = []

    # Utiliser Service pour spécifier le chemin du ChromeDriver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)  # Passer le service au lieu du chemin directement

    driver.get(BASE_URL)

    # Accepter les cookies
    driver.find_element(By.ID, "didomi-notice-agree-button").click()  # Utiliser By.ID

    for name in names:
        # Rechercher l'entreprise
        searchbar = driver.find_element(By.ID, "input_search")  # Utiliser By.ID
        searchbar.send_keys(name)
        searchbar.send_keys(Keys.ENTER)

        # Sélectionner le premier résultat
        driver.find_element(By.CLASS_NAME, "ResultBloc__link__content").click()  # Utiliser By.CLASS_NAME

        # Extraire l'adresse
        address = driver.find_element(By.ID, "adressHover").find_elements(By.CLASS_NAME,
                                                                          "adressText")  # Utiliser By.ID et By.CLASS_NAME
        full_address = " ".join([element.get_attribute("textContent") for element in address])
        addresses.append(full_address.strip())

    # Fermer le navigateur
    driver.quit()

    return addresses
