from bs4 import BeautifulSoup
import requests

# I could use lat and long as parameter?¿
    # Not very user friendly
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
