import nextcord
from nextcord.ext import commands
import random

class Sus(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def sus(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = "Sus-O-Meter",
      description = f"{member.mention} is **{random.randint(1, 100)}%** sus!",
      color = nextcord.Color.random()
    )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/948235933709373470/948605021593940019/images-removebg-preview.png")
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Sus(client))