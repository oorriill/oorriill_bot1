import discord
from discord.ext import commands
import random
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! ecologist bot!')
@bot.command()
async def plastic(ctx):
    await ctx.send(f'Среднее время разложения пластмассовых изделий, колеблется от 6 месяцев до 700 лет.')
@bot.command()
async def glass(ctx):
    await ctx.send(f'Стекло разлагается более тысячи лет!')
@bot.command()
async def rubber(ctx):
    await ctx.send(f'Резина разлагается около сотни лет!')
@bot.command()
async def sorting(ctx):
    await ctx.send(f'Цветовые обозначения баков: желтый – пластик; зеленый – несортированные коммунальные отходы; оранжевый – опасные отходы; синий – макулатура; красный – стекло; серый – электрооборудование, вышедшее из строя. Существует упрощенная система для сбора мусора: серые контейнеры – для органики, синие либо оранжевые – для сухих твердых отходов. Для повышения сознательности граждан при сборе пластика используют сетчатые контейнеры. В сетку собираются отходы одного вида: благодаря прозрачности, люди видят, что именно туда выкидывать.')
bot.run("")
