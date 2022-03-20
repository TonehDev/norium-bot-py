import nextcord
from nextcord.ext import commands

class Grename(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def grename(self, ctx, *, name):
    await ctx.guild.edit(name=name)
    embed = nextcord.Embed(
      title = "Renamed",
      description = f"The guild has been renamed to ``{name}``!",
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

  # Error Handling

  @grename.error
  async def grename_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
        )
        embed.add_field(name = "Usage", value = "``;grename <new_name>``", inline = False)
        embed.add_field(name = "Example", value = "``;grename Our new Discord server``", inline = False)
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

      elif isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
          title = "No Permissions",
          description = "You are missing the ``MANAGE_CHANNELS`` permission.",
          color = nextcord.Color.red()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Grename(client))