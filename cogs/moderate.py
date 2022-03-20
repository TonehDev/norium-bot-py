import nextcord
from nextcord.ext import commands

class Moderate(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_nicknames = True)
  async def moderate(self, ctx, member : nextcord.Member, *, nick = "Moderated Nickname"):
    await member.edit(nick=nick)
    embed = nextcord.Embed(
      title = "Moderated Nickname",
      description = f"Successfully moderated {member.mention}'s nickname!",
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

  # Error Handling

  @moderate.error
  async def moderate_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;moderate @<member> <nickname>``", inline = False)
      embed.add_field(name = "Example", value = "``;moderate @BestGamer WorstGamer``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_NICKNAMES`` permission.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
      embed = nextcord.Embed(
        title = "Member Not Found",
        description = f"No member named ``{ctx.member.name}#{ctx.member.discriminator}`` found.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Moderate(client))