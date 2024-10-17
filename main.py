# Copyright 2024 Angie Tran, Diego Cid
#
# This file is part of Beach Buddy.
# Beach Buddy is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Free Software Foundation, either version 1 of the License, or
# (at your option) any later version.
#
# Beach Buddy is distributed in the hope that it will be useful,
# but WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# See the MIT License for more details.
#
# You should have received a copy of the MIT License
# along with Beach Buddy. If not, see <https://mit-license.org/>.

"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""

import asyncio
import threading
from typing import Literal

from discord import app_commands
from discord.ext import commands

from config import BOT_TOKEN
from course_utils import *
from discord_utils import *
from paginator import PaginatorView
from scrape_subjects import *
from utils import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

subjects_csv = "subjects.csv"
scheduled_scraping = False


def scrape():
    current_date = get_date()
    start_time = time.time()
    print("Scraping...")
    subjects_file = "subjects.csv"
    scrape_fall(subjects_file)
    scrape_spring(subjects_file)
    print("Complete")
    scrape_time = time.time() - start_time
    print(f"--- {scrape_time} seconds for scrape --- @ {current_date} {get_time()}")
    return scrape_time


def scheduled_scrape():
    global scheduled_scraping
    # Schedules scrape at 5:03am - 5:04am PST AKA 12:03pm - 12:04pm UTC
    current_time = get_time()
    if '12:03:00' <= current_time <= '12:04:00':
        scrape_time = scrape()
        asyncio.run_coroutine_threadsafe(notify_scrape(), bot.loop)
        schedule_next_scrape(86400 - (scrape_time + 30))
    else:
        schedule_next_check()
    scheduled_scraping = False


def schedule_next_check():
    global scheduled_scraping
    if not scheduled_scraping:
        threading.Timer(1, scheduled_scrape).start()
        scheduled_scraping = True


def schedule_next_scrape(delay):
    global scheduled_scraping
    if not scheduled_scraping:
        threading.Timer(delay, scheduled_scrape).start()
        scheduled_scraping = True


@bot.event
async def on_ready():
    print("Beach Buddy is awake!")
    if check_days_last_scrape():
        print("It's been longer than 2 days.")
        scrape()
        await notify_scrape()
    scheduled_scrape()
    initialize_caches()


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await ctx.defer()
    await bot.tree.sync()
    await ctx.send("Synced successfully!")


@bot.hybrid_command()
async def ping(ctx, test: Literal['PONG', 'PANG']):
    await ctx.send(f"{test}")


@bot.hybrid_command()
async def set_notif_channel(ctx, channel: discord.TextChannel):
    channel_id = channel.id
    guild_id = ctx.guild.id
    save_notif_channel(guild_id, channel_id)
    await ctx.send(f"Notification channel set to {channel.mention}")


async def notify_scrape():
    try:
        with open('notif.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                guild = bot.get_guild(int(data[0]))
                if guild:
                    channel = guild.get_channel(int(data[1]))
                    await channel.send(f"Schedule Updated ({get_time()})")
    except Exception as e:
        print(f"An error occurred: {e}")


@bot.hybrid_command(name="search", description="Search for course information")
@app_commands.describe(
    season="The academic season",
    abbreviation="The abbreviation of the course. Exclude slashes & spaces.",
    code="The course code",
    opened_only="Show only opened courses"
)
async def search(ctx: commands.Context, season: Literal["Fall 2024", "Spring 2025"], abbreviation: str,
                 code: str, opened_only: Literal["True", "False"]):
    start_time = time.time()
    embeds = []
    abbreviation = abbreviation.upper()
    season = format_season(season)
    if not check_existing_abbreviation(season, abbreviation):
        await ctx.send(f"Invalid abbreviation or this subject does not exist in this season")
        return
    code_list = (get_course_codes(season, abbreviation))
    if code not in code_list:
        await ctx.send(f"Invalid code.")
        return
    course_infos = []
    if season == "fall_2024":
        course_infos = CLASS_CACHE_FALL[f"{abbreviation} {code}"]
    elif season == "spring_2025":
        course_infos = CLASS_CACHE_SPRING[f"{abbreviation} {code}"]
    else:
        print("An unexpected error occurred while getting course infos")
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
        command_time = time.time() - start_time
        print("--- %s seconds for search command ---" % command_time)
        view = PaginatorView(embeds)
        await ctx.send(embed=view.initial, view=view)


@bot.hybrid_command(name="search_by_professor", description="Search for courses taught by a specific professor")
@app_commands.describe(
    season="The academic season",
    last_name="Professor's last name",
    abbreviation="The subject abbreviation",
    opened_only="Show only opened courses"
)
async def search_by_professor(ctx: commands.Context, season: Literal["Fall 2024", "Spring 2025"], last_name: str,
                              abbreviation: str, opened_only: Literal["True", "False"]):
    start_time = time.time()
    season = format_season(season)
    embeds = []
    abbreviation = abbreviation.upper()

    if "spring" in season:
        CLASS_CACHE = CLASS_CACHE_SPRING
    elif "summer" in season:
        CLASS_CACHE = CLASS_CACHE_SUMMER
    elif "fall" in season:
        CLASS_CACHE = CLASS_CACHE_FALL
    else:
        print("Could not find cache for this season")
        return
    course_infos = get_all_prof_course(last_name, abbreviation, CLASS_CACHE)

    if not check_existing_abbreviation(season, abbreviation):
        await ctx.send(f"Invalid abbreviation or this subject does not exist in this season")
        return

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
        command_time = time.time() - start_time
        print("--- %s seconds for search command ---" % command_time)
        view = PaginatorView(embeds)
        await ctx.send(embed=view.initial, view=view)

bot.run(BOT_TOKEN)
