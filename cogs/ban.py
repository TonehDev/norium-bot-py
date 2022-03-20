import nextcord
from nextcord.ext import commands

class Ban(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["b"])
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member : nextcord.Member, *, reason="No reason provided."):
    embed = nextcord.Embed(
      title = "Ban", 
      description = f"Successfully banned user ``{member.name}#{member.discriminator}``.", 
      color = nextcord.Color.green()
    )
    embed.add_field(name = "Reason", value = f"{reason}")
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)

    embed = nextcord.Embed(
      title = "You were banned",
      description = "⚠️ You have been banned from a guild. More information below.",
      color = nextcord.Color.red()
    )
    embed.add_field(
        name = "Guild",
        value = f"{ctx.guild.name}",
        inline = False
    )
    embed.add_field(
        name = "Moderator",
        value = f"{ctx.author.mention}",
        inline = False
    )
    embed.add_field(
        name = "Reason",
        value = f"{reason}",
        inline = False
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await member.send(embed=embed)
    await member.ban(reason=reason)

  @commands.command(aliases=["ub"])
  @commands.has_permissions(ban_members = True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = nextcord.Embed(
                title = "Unban",
                description = f"Successfully unbanned user ``{member.name}#{member.discriminator}``.",
                color = nextcord.Color.green()
            )
            embed.add_field(
                name = "Moderator",
                value = f"{ctx.author.mention}"
            )
            embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
            await ctx.send(embed=embed)
            return

  # Error Handling

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;ban @<user> [reason]``", inline = False)
      embed.add_field(name = "Example", value = "``;ban @BestGamer mass pinging``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``BAN_MEMBERS`` permission.",
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

  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;unban <user>#<tag>``", inline = False)
      embed.add_field(name = "Example", value = "``;unban BestGamer#1902``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``BAN_MEMBERS`` permission.",
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
  client.add_cog(Ban(client))