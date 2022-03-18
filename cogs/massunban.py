import nextcord
from nextcord.ext import commands

class MassUnban(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def massunban(self, ctx):
    banlist = await ctx.guild.bans()
    for users in banlist:
      try:
        await ctx.guild.unban(user=users.user)
      except:
        pass
    embed = nextcord.Embed(
      title = "Unbanned all Members",
      description = "We've managed to unban all members on this server.",
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

  # Error Handling

  @massunban.error
  async def massunban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
          title = "No Permissions",
          description = "You are missing the ``BAN_MEMBERS`` permission.",
          color = nextcord.Color.red()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(MassUnban(client))