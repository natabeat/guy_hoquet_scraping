from bs4 import BeautifulSoup

def parse_data(raw_data):
    soup = BeautifulSoup(raw_data, 'html.parser')
    results = []
    # Logique pour extraire les données d'intérêt
    for item in soup.find_all('div', class_='item'):
        title = item.find('h2').text
        price = item.find('span', class_='price').text
        results.append({
            'title': title,
            'price': price
        })
    return results
