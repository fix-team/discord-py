import discord
from ai import askgpt

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
#     await message.channel.send("Hello World!")

log = None


@client.event
async def on_message(message):
    if message.author.bot:
        return

    global log
    answer, log = askgpt(message.content, log)
    await message.channel.send(answer)

client.run(BOT_TOKEN)
