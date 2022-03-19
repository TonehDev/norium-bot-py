import nextcord
from nextcord.ext import commands

class Start(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed = nextcord.Embed(
        title = "Unknown Command",
        description = f"No command named ``{ctx.message.content}`` found.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(activity=nextcord.Activity(
        type=nextcord.ActivityType.listening, name=";help"))
    print(self.client.user.name + " is now online.")

def setup(client):
  client.add_cog(Start(client))
