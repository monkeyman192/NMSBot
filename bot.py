import discord
from discord.ext import commands
import random
import asyncio
from functions import *

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
@asyncio.coroutine
def rgb(R: float, G: float, B: float, *A: float):
    """Convert NMS format RGB to the usual expression"""
    if not (0 <= R and R <= 1) or not (0 <= G and G <= 1) or not (0 <= B and B <= 1):
        yield from bot.say("Please enter a valid colour (ie. value between 0 and 1 inclusive)")
    else:
        data = NMStoRGB(R, G, B, *A)
        yield from bot.say(data)

@bot.command()
@asyncio.coroutine
def nms(R: float, G: float, B: float, *A: float):
    """Convert the usual format of RGB colour to NMS format"""
    if not (0 <= R and R <= 255) or not (0 <= G and G <= 255) or not (0 <= B and B <= 255):
        yield from bot.say("Please enter a valid colour (ie. value between 0 and 255 inclusive)")
    else:
        data = RGBtoNMS(R, G, B, *A)
        yield from bot.say(data)

@bot.command()
@asyncio.coroutine
def nmsh(hex_str: str):
    """Convert a hex representation of a colour to NMS colour code."""
    if len(hex_str) != 6:
        yield from bot.say("Hex colour format incorrect, please use format 123456 (ie. must always have 6 characters).")
    else:
        R, G, B = HextoNMS(hex_str)
        data = NMS_colour_struct(R, G, B)
        yield from bot.say(data)

bot.run('token_witheld')      # token for test server. the required token is pasted here.

