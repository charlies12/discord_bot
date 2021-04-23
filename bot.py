import os
import discord
import random

TOKEN = os.environ.get('DISCORD_TOKEN')
# GUILD = os.environ.get('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to discord.")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server."
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gacha_games = [
        "Azur Lane",
        "Fate Grand Order",
        "Arknights"
    ]

    if message.content == "recommend gacha" or message.content == "gacha?":
        response = random.choice(gacha_games)
        await message.channel.send(f'Try {response}')

    # elif message.content == "raise-exception":
    #     raise discord.DiscordException

client.run(TOKEN)
