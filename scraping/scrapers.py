from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importer Service
from selenium.webdriver.common.by import By  # Importer By
from selenium.webdriver.common.keys import Keys
from config.settings import CHROMEDRIVER_PATH, BASE_URL, BASE_URL_TEST
import time


def scrape_guy_hoquet():
    #initialisation
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)
    time.sleep(2)

    #accept cookies
    try:
        cookies_button = driver.find_element(By.ID, "tarteaucitronPersonalize2")
        cookies_button.click()
        print("Cookies acceptés")
        time.sleep(2)
    except Exception as e:
        print(f"Erreur lors de l'acceptation des cookies : {e}")

    #go to announces page
    try:
        button_announces = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.form-field")
        button_announces.click()
        print("Accès aux annonces")
        time.sleep(2)
    except Exception as e:
        print(f"Erreur lors de l'accès aux annonces : {e}")
        driver.quit()
        return

    #retrieve all announces
    try:
        announce_cards = driver.find_elements(By.CLASS_NAME, "property_link_block")
        for card in announce_cards:
            url = card.get_attribute("href")
            print(f"Annonce trouvée : {url}")
            driver.get(url)
            time.sleep(2)
            #get title
            try:
                title = driver.find_element(By.CLASS_NAME, "name.property-name").text
                print(f"Titre de l'annonce : {title}")
            except Exception as e:
                print(f"Erreur lors de la récupération du titre de l'annonce : {e}")
            #get summary
            #(click on 'Voir plus' before)
            try:
                description_more = driver.find_element(By.CLASS_NAME, "description-minus").text
                print(f"Résumé : {description_more}")
            except Exception as e:
                print(f"Erreur lors de la récupération du résumé : {e}")

            #get location
            try:
                location = driver.find_element(By.CLASS_NAME, "add").text
                print(f"Localisation : {location}")
            except Exception as e:
                print(f"Erreur lors de la récupération de la localisation de l'annonce : {e}")
            #get price
            try:
                price = driver.find_element(By.CLASS_NAME, "price").text
                clean_price = price.replace("*", "")
                print(f"Prix : {clean_price}")
            except Exception as e:
                print(f"Erreur lors de la récupération du prix de l'annonce : {e}")

            #get photos
            print('-------------Annonce suivante-------------')
            driver.back()
            time.sleep(2)
    except Exception as e:
        print(f"Erreur lors de la récupération des liens d'annonces : {e}")
    driver.quit()


def scrape_addresses(names):
    addresses = []

    # Utiliser Service pour spécifier le chemin du ChromeDriver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)  # Passer le service au lieu du chemin directement

    driver.get(BASE_URL_TEST)

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
