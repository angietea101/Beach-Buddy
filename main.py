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
from paginator import PaginatorView


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
    embeds = []
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
    # Turn the course list into a long string to be sent back to user
    if opened_only == "True":
        for course in course_infos:
            course_stripped = course.open_seats.strip()
            if course_stripped != "NONE":
                embed = discord.Embed(title=f"{course.course_abr}: {course.course_name} {course.type} ({course.units})",
                                      color=discord.Color.dark_blue())
                embed.add_field(name="Professor:", value=f"{course.instructor}")
                embed.add_field(name="Section Number:", value=f"{course.course_section}")
                embed.add_field(name="Course Number:", value=f"{course.course_number}")
                embed.add_field(name="Reserved Seats:", value=f"{course.reserved_cap}")
                embed.add_field(name="Open Seats:", value=f"{course.open_seats}")
                embed.add_field(name="Location:", value=f"{course.location}")
                embed.add_field(name="Days:", value=f"{course.days}")
                embed.add_field(name="Time:", value=f"{course.time}")
                embed.add_field(name="Additional Notes:", value=f"{course.comment}")
                embeds.append(embed)
    else:
        for course in course_infos:
            embed = discord.Embed(title=f"{course.course_abr}: {course.course_name} {course.type} ({course.units})",
                                  color=discord.Color.dark_blue())
            embed.add_field(name="Professor:", value=f"{course.instructor}")
            embed.add_field(name="Section Number:", value=f"{course.course_section}")
            embed.add_field(name="Course Number:", value=f"{course.course_number}")
            embed.add_field(name="Reserved Seats:", value=f"{course.reserved_cap}")
            embed.add_field(name="Open Seats:", value=f"{course.open_seats}")
            embed.add_field(name="Location:", value=f"{course.location}")
            embed.add_field(name="Days:", value=f"{course.days}")
            embed.add_field(name="Time:", value=f"{course.time}")
            embed.add_field(name="Additional Notes:", value=f"{course.comment}")
            embeds.append(embed)
    if len(embeds) == 0:
        await ctx.send("No results were found.")
    else:
        view = PaginatorView(embeds)
        await ctx.send(embed=view.initial, view=view)



bot.run(BOT_TOKEN)
