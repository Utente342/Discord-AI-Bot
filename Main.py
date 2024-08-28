import discord
from discord.ext import commands
import google.generativeai as genai

intents = discord.Intents.default()
intents.message_content = True

genai.configure(api_key="API KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ask(ctx, * ,arg ):
    response = model.generate_content(arg)
    await ctx.send(response.text)

bot.run("DISCORD BOT KEY")
