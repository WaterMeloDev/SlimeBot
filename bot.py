import discord
import os
import asyncio

from itertools import cycle
from discord.ext import commands, tasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix='>', intents=discord.Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
    try: 
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands!")
    except:
        print(f'already synced')
    print(f"Connected to {client.user}!")
    change_status.start()

# Load cogs
async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

# Bot status cycle
status = cycle([
    'Sliming around',
    'Sticky situations',
    'Living that slime life',
    'Dripping with enthusiasm',
    'Gooey adventures',
    'Slime and shine',
    'Getting slimy',
    'Squishy endeavors',
    'Slimetastic moments',
    'Embracing the ooze',
    'Sliming through the day',
    'Stuck in a slime loop',
    'Slippery situations',
    'Squirming with delight',
    'Feeling slime-tastic',
    'Dancing in the slime light',
    'Squelching through tasks',
    'Globbing onto new ideas',
    'Sliming with creativity',
    'Oozing positivity',
    'Molding the future',
    'Squelching through challenges',
    'Sloshing with joy',
    'Glooping along'
])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status), status=discord.Status.online))


async def main():
    async with client:
        try:
            await load_cogs()
        except Exception as e:
            print(f"Error loading cogs: {e}")
        await client.start(discord_token)

# Run the main function
asyncio.run(main())
