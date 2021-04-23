import os
import discord

TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    # guild = discord.utils.get(client.guilds, name=GUILD)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f"{client.user} is connected to the following guild:\n"
          f"{guild.name} (id: {guild.id})")
    # print(f"{client.user} has connected to Discord.")

    members = '\n - '.join([member.name for member in guild.members])
    print(f"Guild members:\n - {members}")

client.run(TOKEN)
