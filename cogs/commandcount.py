import nextcord
from nextcord.ext import commands

class CommandCount(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["count", "commands", "cmd"])
  async def commandcount(self, ctx):
    embed = nextcord.Embed(
      title = "Command Count",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "Total Commands", value = "46", inline = False)
    embed.add_field(name = "Excluding Help Commands", value = "40", inline = False)
    embed.add_field(name = "Excluding This Command and Help Commands", value = "39", inline = False)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CommandCount(client))