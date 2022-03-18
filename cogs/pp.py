import nextcord
from nextcord.ext import commands
import random

class ppRate(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def pp(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    pp = [
      "8D",
      "8=D",
      "8==D",
      "8===D",
      "8====D",
      "8=====D",
      "8======D",
      "8=======D",
      "8========D",
      "8=========D",
      "8==========D",
      "8===========D",
      "8============D",
      "8=============D",
      "8==============D",
      "8===============D",
      "8================D",
      "8=================D",
      "8==================D",
      "8===================D",
      "8====================D",
      "8=====================D",
      "8======================D",
      "8=======================D",
      "8========================D",
      "8=========================D",
      "8==========================D"
    ]
    embed = nextcord.Embed(
      title = f"PP-O-Meter",
      description = f"{member.mention}'s PP Size\n{random.choice(pp)}",
      color = nextcord.Color.random()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(ppRate(client))