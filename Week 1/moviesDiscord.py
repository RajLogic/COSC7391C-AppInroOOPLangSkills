import discord
from imdb import Cinemagoer

im = Cinemagoer()

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hello!")



bot.run("your token here")