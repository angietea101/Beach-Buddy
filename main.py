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

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Beach Buddy is awake!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@bot.tree.command(name="search")
@app_commands.describe(course="What is the course abbreviation + code? [EX: MATH 100]")
async def search(interaction: discord.Interaction, course: str):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! You requested for {course}.")


def main():
    bot.run(BOT_TOKEN)
    # fall_path = "seasons/fall_2024"
    # summer_path = "seasons/summer_2024"
    # subjects_csv = "subjects.csv"
    # subjects_abbreviation = csv_to_dictionary(subjects_csv)
    # print(subjects_abbreviation)


if __name__ == "__main__":
    main()
