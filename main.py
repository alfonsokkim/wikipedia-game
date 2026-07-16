from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Step 0: Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Step 1: bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Step 2: message functionality
async def send_message(message: Message, user_message: str) -> None:   
    if not user_message:
        print('(message was empty because intents were not enabled probably)')
        return

    try:
        response = get_response(user_message)
        if response:
            for link in response:
                await message.channel.send(link)
    except Exception as e:
        print(e)

# Step 3: handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Step 4: handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# Step 5: Main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()