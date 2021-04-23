import os
import random
from discord.ext import commands

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


# shows connection
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to discord.")


# greetings to people joining server
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server."
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    gacha_games = [
        "Azur Lane",
        "Fate Grand Order",
        "Arknights"
    ]
    # recommend a gacha game from previous list
    if message.content == "recommend gacha" or message.content == "gacha?":
        response = random.choice(gacha_games)
        await message.channel.send(f'Try {response}')

    # elif message.content == "raise-exception":
    #     raise discord.DiscordException

bot.run(TOKEN)
