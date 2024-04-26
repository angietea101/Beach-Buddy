"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""
import discord
from discord import app_commands
from discord.ext import commands
from utils import csv_to_dictionary
from config import BOT_TOKEN
from typing import Literal

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

fall_path = "seasons/fall_2024"
summer_path = "seasons/summer_2024"
subjects_csv = "subjects.csv"
subjects_abbreviation = csv_to_dictionary(subjects_csv)
subjects_keys_list = list(subjects_abbreviation.keys())


@bot.event
async def on_ready():
    print("Beach Buddy is awake!")


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing...")
    await bot.tree.sync()
    await ctx.send("Synced successfully")


@bot.hybrid_command()
async def ping(ctx, test: Literal['PONG', 'PANG']):
    await ctx.send(f"{test}")


@bot.hybrid_command()
async def search(ctx: commands.Context, abbreviation: str, code: int):
    abbreviation = abbreviation.upper()
    if abbreviation not in subjects_abbreviation:
        await ctx.send(f"Invalid abbreviation. Examples: MATH, CECS, or BIOL")
        return
    else:
        await ctx.send(f"Valid abbreviation.")


bot.run(BOT_TOKEN)
