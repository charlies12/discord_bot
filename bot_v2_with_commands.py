import os
import random
from discord.ext import commands

TOKEN = os.environ.get('DISCORD_TOKEN')

# prefix for bot will be a ? mark
bot = commands.Bot(command_prefix='?')


# shows connection
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to discord.")


# no command here
# greetings to people joining server
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server."
    )


# using command here
# recommend a gacha game
@bot.command(name="gacha", help="Just a few gacha games I've been recommended.")
async def recommendations(ctx):
    gacha_games = [
        "Azur Lane",
        "Fate Grand Order",
        "Arknights"
    ]

    response = random.choice(gacha_games)
    await ctx.send(f'Try {response}')


bot.run(TOKEN)
