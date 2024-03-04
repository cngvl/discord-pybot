from discord import Intents, Client, Message
from responses import get_responses
from petrol_scrape import petrol_scrape_print
from dotenv import load_dotenv
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
        if is_private:
            await message.author.send(response)
        # else:
        #     await message.channel.send(response)
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

    if user_message.startswith('$petty') and len(user_message) == 11:
        await message.channel.send(petrol_scrape_print(user_message))
        print('Finished petrol_scrape_print')

    print(f'[{channel}] - {username}: "{user_message}" ')

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
