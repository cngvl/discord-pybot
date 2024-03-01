from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os

# I could use lat and long as parameter?¿
    # Not very user friendly

load_dotenv()
WEATHER_TOKEN = os.getenv('OPENWEATHER_TOKEN')

def get_lat_long(postCode: str) -> list:
    # url = f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={WEATHER_TOKEN}'
    url = f'https://api.openweathermap.org/geo/1.0/zip?zip={postCode},AU&appid={WEATHER_TOKEN}'
    page = requests.get(url).json()
    # print(page.json()['lat'])
    # print(page.json()['lon'])

    latlong = [page['lat'], page['lon']]
    print(latlong)

    return latlong

get_lat_long('3020')

def petrol_scrape() -> str:
    url = 'https://petrolspy.com.au/map/latlng/-37.792503416413055/144.82380823806795'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    header = soup.find('h3' , id='main-station-list-header').text
    box = soup.find('table', id='main-station-list-table')
    rows = box.find_all('td')

    returnText = f'{header}\n\n'

    for row in range(0, len(rows) - 1, 2):
        returnText += f'- {rows[row].text}\n{rows[row + 1].text}\n\n'

    # print(returnText)

    return returnText

# petrol_scrape()
