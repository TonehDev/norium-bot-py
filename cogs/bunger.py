import nextcord
from nextcord.ext import commands

class Bunger(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def bunger(self, ctx):
    embed = nextcord.Embed(
      title = "Bunger :hamburger:", 
      description = "Bunger :hamburger:", 
      color = nextcord.Color.gold()
    )
    embed.set_image(
      url = "https://cdn.discordapp.com/attachments/853196607548555285/875999967838343198/tenor.gif"
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Bunger(client))