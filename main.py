import keep_alive
import nextcord
from nextcord.ext import commands
import os


client  = commands.Bot(command_prefix = ".")
client.remove_command("help")
token = os.environ["TOKEN"]

@client.command()
@commands.is_owner()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Loaded 1 command",
    description = "Successfully loaded 1 command!",
    color = nextcord.Color.blurple()
  )
  embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
  await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Unloaded 1 command",
    description = "Successfully unloaded 1 command!",
    color = nextcord.Color.blurple()
  )
  embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
  await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Reloaded 1 command",
    description = "Successfully reloaded 1 command!",
    color = nextcord.Color.blurple()
  )
  embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
  await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# help command

@client.group(invoke_without_command = True)
async def help(ctx):
  
    embed = nextcord.Embed(
      title = "Help Menu",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "Moderation", value = "``.help moderation``", inline = "false")
    embed.add_field(name = "Misc", value = "``.help misc``", inline = "false")
    embed.add_field(name = "Utility", value = "``.help utility``", inline = "false")
    embed.add_field(name = "Fun", value = "``.help fun``", inline = "false")
    embed.add_field(name = "Server Management", value = "``.help management``", inline = "false")
    embed.add_field(name = "More Information", value = "[Support Server](https://discord.gg/pZhk8rMrz7)\n[Read the Docs](https://noriumbot-readthedocs.github.io/docs/)", inline = "false")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
    embed = nextcord.Embed(
      title = "Moderation Plugin",
      description = "``<> Required``\n``[] Optional``",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "``.warn @<member> [reason]``", value = "Warn a member")
    embed.add_field(name = "``.mute @<member> [reason]``", value = "Mute a member")
    embed.add_field(name = "``.lock <reason>``", value = "Lock the current channel in which you are in")
    embed.add_field(name = "``.ban @<member> [reason]``", value = "Ban a member from your server")
    embed.add_field(name = "``.kick @<member> [reason]``", value = "Kick a member from your server")
    embed.add_field(name = "``.unmute @<member>``", value = "Unmute a member that was timed out",)
    embed.add_field(name = "``.clear <msg_amount>``", value = "Clear several messages at once")
    embed.add_field(name = "``.unban <user>#<discriminator>``", value = "Unban a member from your server")
    embed.add_field(name = "``.unlock``", value = "Unlock a channel")
    embed.add_field(name = "``.moderate @<member>``", value = "Moderate a member's nickname")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@help.command()
async def misc(ctx):
    embed = nextcord.Embed(
      title = "Misc Plugin",
      description = "``<> Required``\n``[] Optional``",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "``.ping``", value = "Shows client latency")
    embed.add_field(name = "``.about``", value = "Information about Norium Bot")
    embed.add_field(name = "``.serverinfo``", value = "Information about the current guild")
    embed.add_field(name = "``.links``", value = "All Norium Bot related links")
    embed.add_field(name = "``.version``", value = "The current version Norium Bot is on")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    embed = nextcord.Embed(
      title = "Fun Plugin",
      description = "``<> Required``\n``[] Optional``",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "``.bunger``", value = "Bunger :hamburger:")
    embed.add_field(name = "``.8ball <question>``", value = "Ask the almighty 8ball a question")
    embed.add_field(name = "``.sus @[member]``", value = "Sus-O-Meter :flushed:")
    embed.add_field(name = "``.pp @[member]``", value = "PP-O-Meter")
    embed.add_field(name = "``.gayrate @[member]``", value = "See how gay you are or another member is")
    embed.add_field(name = "``.kill @<member>``", value = "Make someone unalive")
    embed.add_field(name = "``.cat``", value = "Sends random cat images")
    embed.add_field(name = "``.dog``", value = "Sends random dog images")
    embed.add_field(name = "``.simprate``", value = "See how much of a simp you are or another member is")
    embed.add_field(name = "``.coinflip``", value = "Flip a coin")
    embed.add_field(name = "``.minecraft``", value = "Get a minecraft player's profile")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@help.command()
async def management(ctx):
    embed = nextcord.Embed(
      title = "Server Management Plugin",
      description = "``<> Required``\n``[] Optional``",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "``.slowmode <value_in_seconds>``", value = "Set the slowmode in seconds (e.g. .slowmode 3600)")
    embed.add_field(name = ":warning: ``.txtnuke``", value = "**This command has been marked as dangerous.**\nNukes all text channels\n**We recommend you only perform this command in a staff channel.**")
    embed.add_field(name = "``.grename <new_name>``", value = "Renames the guild")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@help.command()
async def utility(ctx):
    embed = nextcord.Embed(
      title = "Utility Plugin",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "``.poll <option_1> <option_2> <topic>``", value = "Send a voting message")
    embed.add_field(name = "``.guildcount``", value = "Shows the amount of servers Norium Bot is in")
    embed.add_field(name = "``.sayembed <text>``", value = "Send a custom embed with title and description")
    embed.add_field(name = "``.template``", value = "A basic rule template incase you don't have rules already or don't know what rules you should put")
    embed.add_field(name = "``.profile @[member]``", value = "Your's or another user's profile")
    embed.add_field(name = "``.avatar @[member]``", value = "Displays your avatar or another member's avatar")
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(manage_channels = True)
async def txtnuke(ctx):
  embed = nextcord.Embed(
    title = ":warning: Are you sure?",
    description = "All changes are irreversible, we are not responsible for any damage done to your server.",
    color = nextcord.Color.red()
  )
  embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")

  view = Confirm()
  await ctx.send(embed=embed, view=view)

  await view.wait()

  if view.value == True:
      for c in ctx.guild.channels:
        await c.delete()

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
  
    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Deleting channels...", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
          title = "Cancelling...",
          description = "Process cancelled.",
          color = nextcord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.value = False
        self.stop()

@txtnuke.error
async def txtnuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_CHANNELS`` permission.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
      await ctx.send(embed=embed)

  
@client.command()
async def about(ctx):
    embed = nextcord.Embed(
      title = "Norium Bot",
      description = "A multi-purposed, actively developed Discord Bot.\nMade by **Toneh#3391**.",
      color = nextcord.Color.blue()
    )
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/779402361734692914/875018579853074443/norium4.png")
    await ctx.send(embed=embed)

  
keep_alive.keep_alive()
client.run(token)
