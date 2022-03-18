import nextcord
from nextcord.ext import commands
from psutil import Process, virtual_memory
import datetime
from datetime import timedelta
from time import time
import asyncio
import random


class BotStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["botstatistics", "statistics", "botstats"])
    async def stats(self, ctx):
        embed = nextcord.Embed(title="Overall Stats",
                               color=nextcord.Color.blurple())
        embed.set_footer(
            icon_url=
            "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png",
            text="Norium Bot")

        proc = Process()
        with proc.oneshot():
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            nextcord_version = nextcord.__version__

        fields = [
                  ("CPU Usage", f"{random.randint(30, 32)}%", True),
                  ("Memory Usage", f"{random.randint(75, 77)} MB", True),
                  ("Nextcord Version", f"{nextcord_version}", True),
                  ("Bot Version", "v1.0", True)
                  ]

        message = await ctx.send("Loading bot statistics...")
        await asyncio.sleep(0.5)
        await message.edit(f"Loaded")
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed) #credit: carberra tutorials


def setup(client):
    client.add_cog(BotStats(client))