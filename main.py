from bs4 import BeautifulSoup
import requests
from discord import Intents, Client, Message
from responses import get_responses
from dotenv import load_dotenv
# import discord
import os


# Loading token from env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty')
        return

    if is_private := user_message[0] == '?':  # Walrus operator
        user_message = user_message[1:]

    try:
        response = get_responses(user_message)
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)

# Handling startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming messages
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] - {username}: "{user_message}" ')
    await send_message(message, user_message)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
















# url = 'https://petrolspy.com.au/map/latlng/-37.792503416413055/144.82380823806795'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# box = soup.find('table', id='main-station-list-table')
# rows = box.find_all('td')
# # print(rows[1])

# for row in range(0, len(rows) - 1, 2):
#     print(rows[row].text)
#     print(f'{rows[row + 1].text}\n' )

# class MyClient(Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

# intents = Intents.default()
# intents.message_content = True

# client = Client(intents=intents)
# client.run(token)

# # @client.event
# # async def on_ready() -> None:
# #     print(f'{client.user} is now running!')

# # MyClient.on_ready(client)
# def main() -> None:
#     client.run(token)


# if __name__ == '__main__':
#     main()
