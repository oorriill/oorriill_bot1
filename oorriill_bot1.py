import discord
from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!привет'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('!смайлик'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('!монетка'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('!пароль'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('!лиза'):
        await message.channel.send("Лиза милашка")
client.run("")
