import discord
import os
import requests
print(os.listdir('images'))
import tok
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока!')
@bot.command()
async def pasw(ctx, count = 8):
    await ctx.send(f"Ваш пароль - {gen_pass(count)}")
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong')
@bot.command()
async def coin(ctx):
    await ctx.send(f"{flip_coin()}")
@bot.command()
async def elizabeth(ctx):
    await ctx.send(f'Лиза милашка')
@bot.command()
async def mem1(ctx):
    lst = os.listdir('images1')
    rand_img = random.choice(lst)
    with open('images1/' + rand_img, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
#новая команда#
@bot.command()
async def mem(ctx):
    lst = os.listdir('images')
    rand_img = random.choice(lst)
    with open('images/' + rand_img, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
#новая команда#
bot.run("")
