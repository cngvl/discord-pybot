from bs4 import BeautifulSoup
import requests


def petrol_scrape() -> str:
    url = 'https://petrolspy.com.au/map/latlng/-37.792503416413055/144.82380823806795'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    box = soup.find('table', id='main-station-list-table')
    rows = box.find_all('td')
    # print(rows[1])

    returnText = ''

    for row in range(0, len(rows) - 1, 2):
        returnText += rows[row].text
        returnText += f'{rows[row + 1].text}\n'

    return returnText
