import discord
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
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong')
bot.run("")
