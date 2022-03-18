import nextcord
from nextcord.ext import commands
import random

class GayRate(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def gayrate(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = f"Gay Rate",
      description = f"{member.mention} is **{random.randint(1, 100)}%** gay!",
      color = nextcord.Color.random()
    )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/948235933709373470/948606707926462484/images.png")
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(GayRate(client))