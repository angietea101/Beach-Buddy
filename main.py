"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""
import discord
from discord.ext import commands, tasks
from utils import csv_to_dictionary, get_csv_path, get_course_codes, get_class_infos, create_embed, get_time, save_notif_channel
from config import BOT_TOKEN
from typing import Literal
from paginator import PaginatorView
from scrape_subjects import scrape_fall
from scrape_subjects import scrape_summer

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

subjects_csv = "subjects.csv"
subjects_abbreviation = csv_to_dictionary(subjects_csv)


def scheduled_scrape():
    print("Scraping...")
    subjects_file = "subjects.csv"
    scrape_fall(subjects_file)
    scrape_summer(subjects_file)
    print("Complete")


@bot.event
async def on_ready():
    print("Beach Buddy is awake!")
    notify_scrape.start()


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing...")
    await bot.tree.sync()
    await ctx.send("Synced successfully")


@bot.hybrid_command()
async def ping(ctx, test: Literal['PONG', 'PANG']):
    await ctx.send(f"{test}")

@bot.hybrid_command()
async def notify(ctx, channel: discord.TextChannel):
    channel_id = channel.id
    guild_id = ctx.guild.id
    save_notif_channel(guild_id, channel_id)
    await ctx.send(f"Notification channel set to {channel.mention}")

@tasks.loop(seconds = 1)
async def notify_scrape():
    current_time = get_time()
    if current_time == '05:03:30':
        scheduled_scrape()
        try:
            with open('notif.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    guild = bot.get_guild(int(data[0]))
                    if guild:
                        channel = guild.get_channel(int(data[1]))
                        await channel.send("Schedule Updated")
        except Exception as e:
            print(f"An error occured: {e}")
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
    # Turn the course list into a list of embeds to be relayed back to user
    if opened_only == "True":
        for course in course_infos:
            if course.open_seats != "CLOSED":
                embed = create_embed(course)
                embeds.append(embed)
    else:
        for course in course_infos:
            embed = create_embed(course)
            embeds.append(embed)
    if len(embeds) == 0:
        await ctx.send("No results were found.")
    else:
        view = PaginatorView(embeds)
        await ctx.send(embed=view.initial, view=view)


bot.run(BOT_TOKEN)
