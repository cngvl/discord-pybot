from bs4 import BeautifulSoup
import requests
import discord

# url = 'https://petrolspy.com.au/map/latlng/-37.792503416413055/144.82380823806795'
# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# box = soup.find('table', id='main-station-list-table')

# rows = box.find_all('td')
# # print(rows[1])

# for row in range(0, len(rows) - 1, 2):
#     print(rows[row].text)
#     print(rows[row + 1].text)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
