import nextcord
from nextcord.ext import commands
import random

class SimpRate(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def simprate(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = f"Simp-O-Meter",
      description = f"{member.mention} is **{random.randint(1, 100)}%** a simp!",
      color = nextcord.Color.random()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(SimpRate(client))