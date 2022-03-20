import nextcord
from nextcord.ext import commands

class Slowmode(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["sm"])
  @commands.has_permissions(manage_channels = True)
  async def slowmode(self, ctx, arg : int):
    if arg > 21600:
      embed = nextcord.Embed(
        title = "Can't set Slowmode above 6 hours",
        description = "You cannot set the slowmode above 6 hours!",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.reply.send(embed=embed)
    elif arg == 0:
      embed = nextcord.Embed(
        title = "Toggled Slowmode",
        description = "Slowmode has been turned off.",
        color = nextcord.Color.green()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.reply.send(embed=embed)
    else:
      
      await ctx.channel.edit(slowmode_delay = arg)
      embed = nextcord.Embed(
          title = "Slowmode is now set", 
          description = f"Set the slowmode delay to **{arg}** seconds!", 
          color = nextcord.Color.blurple()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed) #credit: glowstik

  # Error Handling

  @slowmode.error
  async def slowmode_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;slowmode <slowmode_in_seconds>``", inline = False)
      embed.add_field(name = "Example", value = "``;slowmode 3600``", inline = False)
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
  client.add_cog(Slowmode(client))