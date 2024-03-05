from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os

load_dotenv()
WEATHER_TOKEN = os.getenv('OPENWEATHER_TOKEN')

def get_lat_long(user_message: str) -> list:
    # Checking if user_message is in the correct format
    postCode = int(user_message[-4:])

    if not (postCode):
        raise TypeError('Incorrect postcode format')

    url = f'https://api.openweathermap.org/geo/1.0/zip?zip={postCode},AU&appid={WEATHER_TOKEN}'
    page = requests.get(url).json()
    latlong = [page['lat'], page['lon']]

    return latlong

# coords = get_lat_long('$petty 3025')

def petrol_scrape(postCode: str) -> list:
    coords = get_lat_long(postCode)
    url = f'https://petrolspy.com.au/map/latlng/{coords[0]}/{coords[1]}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    header = soup.find('h3' , id='main-station-list-header').text
    box = soup.find('table', id='main-station-list-table')
    rows = box.find_all('td')

    petrolLocations = []
    petrolPrices = []

    for row in range(0, len(rows) - 1, 2):
    #     returnText += f'- {rows[row].text}\n{rows[row + 1].text}\n\n'
        if rows[row].text not in petrolLocations:
            petrolLocations.append(rows[row].text)

        if rows[row + 1].text not in petrolPrices:
            petrolPrices.append(rows[row + 1].text)


    return [header, petrolLocations, petrolPrices]


def petrol_scrape_print(user_message) -> list:
    scrapeInfo = petrol_scrape(user_message)

    returnText = ''

    petrolLocations = scrapeInfo[1]

    for val in range(len(petrolLocations)):
        returnText += f'- {petrolLocations[val]}\n {scrapeInfo[2][val]}\n\n'

    # print(returnText)
    return [scrapeInfo[0] ,returnText]

# user_message = petrol_scrape('$petty 3020')
# petrol_scrape_print('$petty 3020')
