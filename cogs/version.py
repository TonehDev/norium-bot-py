import nextcord
from nextcord.ext import commands

class Version(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["v"])
  async def version(self, ctx):
    version = "v1.0"
    embed = nextcord.Embed(
      title = "Version",
      description = f"Norium Bot is currently on version **{version}**",
      color = nextcord.Color.blurple()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Version(client))