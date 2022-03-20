import nextcord
from nextcord.ext import commands

class Mute(commands.Cog):

  def __init__(self, client):
    self.client = client
     
  @commands.command(aliases=["m"])
  @commands.has_permissions(manage_roles = True)
  async def mute(self, ctx, member : nextcord.Member, *, reason = "No reason provided."):
      guild = ctx.guild
      mutedRole = nextcord.utils.get(guild.roles, name = "Muted")

      if not mutedRole:
        embed = nextcord.Embed(
          title = "Muted Role",
          description = "We could not find the 'Muted' role. Creating one for you...",
          color = nextcord.Color.red()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)
        mutedRole = await guild.create_role(name = "Muted")

        for channel in guild.channels:
          await channel.set_permissions(mutedRole, send_messages = False, speak = False, read_message_history = True, read_messages = True)
          await member.add_roles(mutedRole, reason = reason)

      await member.add_roles(mutedRole, reason=reason)
    
      embed = nextcord.Embed(
        title = "Mute", 
        description = f"Successfully muted user ``{member.name}#{member.discriminator}``.", 
        color = nextcord.Color.green()
      )
      embed.add_field(name = "Reason", value = f"{reason}")
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)
    
      embed = nextcord.Embed(
        title = "You were muted",
        description = f"⚠️ You were muted in a guild. More information below.",
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

  @commands.command(aliases=["um"])
  @commands.has_permissions(manage_roles = True)
  async def unmute(self, ctx, member : nextcord.Member):
    guild = ctx.guild
    mutedRole = nextcord.utils.get(guild.roles, name = "Muted")

    await member.remove_roles(mutedRole)

    embed = nextcord.Embed(
      title = "Unmute", 
      description = f"Successfully unmuted user ``{member.name}#{member.discriminator}``.", 
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)
    embed = nextcord.Embed(
      title = "You were unmuted",
      description = f"You were unmuted in **{ctx.guild.name}**",
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await member.send(embed=embed)

  # Error Handling

  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;mute @<user> [reason]``", inline = False)
      embed.add_field(name = "Example", value = "``;mute @BestGamer swearing``", inline = False)
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

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_ROLES`` permission.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;unmute @<user>``", inline = False)
      embed.add_field(name = "Example", value = "``;unmute @BestGamer``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_ROLES`` permission.",
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
  client.add_cog(Mute(client))