"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""
import discord
from discord import app_commands
from discord.ext import commands
from utils import csv_to_dictionary, get_csv_path, get_course_codes, get_class_infos
from config import BOT_TOKEN
from typing import Literal


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

subjects_csv = "subjects.csv"
subjects_abbreviation = csv_to_dictionary(subjects_csv)


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
async def search(ctx: commands.Context, season: Literal["Fall 2024", "Summer 2024"], abbreviation: str, code: str,
                 opened_only: Literal["True", "False"]):
    abbreviation = abbreviation.upper()
    if season == "Fall 2024":
        season = "fall_2024"
    else:
        season = "summer_2024"
    if abbreviation not in subjects_abbreviation:
        await ctx.send(f"Invalid abbreviation. Examples: MATH, CECS, or BIOL")
        return
    csv_path = get_csv_path(season, abbreviation, subjects_abbreviation)
    code_list = (get_course_codes(csv_path))
    if code not in code_list:
        await ctx.send(f"Invalid code.")
        return
    course_infos = get_class_infos(season, abbreviation, subjects_abbreviation, code)
    response = ""
    # Turn the course list into a long string to be sent back to user
    if opened_only == "True":
        for course in course_infos:
            course_stripped = course.open_seats.strip()
            if course_stripped != "NONE":
                response += str(f"{course}\n")
    else:
        for course in course_infos:
            response += str(f"{course}\n")
    if len(response) == 0:
        await ctx.send("No results were found.")
    else:
        await ctx.send(response)


bot.run(BOT_TOKEN)
