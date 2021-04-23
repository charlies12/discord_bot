import discord
import os
import random

Token = os.environ.get('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    some_words = [
        "Azur Lane",
        "FGO",
        "Arknights"
    ]

    if message.content == "gacha":
        response = random.choice(some_words)
        await message.channel.send(response)

client.run(Token)


if __name__ == '__main__':
    on_message()
