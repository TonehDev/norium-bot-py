import nextcord
from nextcord.ext import commands

class Avatar(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["av"])
  async def avatar(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = f"Avatar for {member}", 
      description = f"{member}'s avatar", 
      color = nextcord.Color.blue()
    )
    embed.set_image(url = member.avatar.url)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Avatar(client))