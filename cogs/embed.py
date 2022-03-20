import nextcord
from nextcord.ext import commands

class CustomEmbed(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def embed(self, ctx, *, msg):
    embed = nextcord.Embed(
      description = f"{msg}",
      color = nextcord.Color.random()
    )
    await ctx.send(embed=embed)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")

  # Error Handling
  @embed.error
  async def embed_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;embed <text>``", inline = False)
      embed.add_field(name = "Example", value = "``;embed Cats are amazing``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CustomEmbed(client))