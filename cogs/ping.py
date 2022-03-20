import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["latency"])
  async def ping(self, ctx):
    embed = nextcord.Embed(
      title = "Latency",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "Client", value = f"{round(self.client.latency * 1000)} ms")
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Ping(client))