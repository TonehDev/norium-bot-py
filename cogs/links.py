import nextcord
from nextcord.ext import commands

class Links(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def links(self, ctx):
    embed = nextcord.Embed(
      title = "Links",
      description = f"[Support Server](https://discord.gg/2xzfZtAKMf)\n[Documentation](https://noriumbot-readthedocs.github.io/docs/)\n[Top.gg Page](https://top.gg/bot/871454184212410408)\n[Vote](https://top.gg/bot/871454184212410408/vote)\n[Invite](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&permissions=402778230&scope=bot)\n[Website](https://noriumbot.github.io/home/)",
      color = nextcord.Color.blurple()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Links(client))