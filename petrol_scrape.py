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

def petrol_scrape(postCode: str) -> str:
    coords = get_lat_long(postCode)
    url = f'https://petrolspy.com.au/map/latlng/{coords[0]}/{coords[1]}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    header = soup.find('h3' , id='main-station-list-header').text
    box = soup.find('table', id='main-station-list-table')
    rows = box.find_all('td')

    returnText = f'{header}\n\n'

    for row in range(0, len(rows) - 1, 2):
        returnText += f'- {rows[row].text}\n{rows[row + 1].text}\n\n'

    return returnText

# petrol_scrape('$petty 3025')
