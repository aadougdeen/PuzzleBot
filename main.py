import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is online.')

@client.command()
async def puzzle(ctx):
    await ctx.send(file=discord.File('momopic.jpg'))

@client.command()
async def alithefurry(ctx):
    await ctx.send(file=discord.File('pringle.jpg'))

client.run('TOKEN')
