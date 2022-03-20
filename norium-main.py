import nextcord
from nextcord.ext import commands
import os
from nextcord.ui import Button
import asyncio
import urllib
import json

intents = nextcord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=";", case_insensitive = True, intents=intents)
client.remove_command("help")
token = "nope"

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title=f"Loaded",
                           description=f"Loaded 1 feature!",
                           color=nextcord.Color.blurple())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title=f"Unloaded",
                           description=f"Unloaded 1 feature!",
                           color=nextcord.Color.blurple())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title=f"Reloaded",
                           description=f"Reloaded 1 feature!",
                           color=nextcord.Color.blurple())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# help command

class HelpDropdown(nextcord.ui.Select):
    def __init__(self):
        selectOptions = [
            nextcord.SelectOption(label = "Moderation", description = "Displays all moderation features", emoji = "🛠️"),
            nextcord.SelectOption(label = "Fun", description = "Displays all fun features", emoji = "🎮"),
            nextcord.SelectOption(label = "Misc", description = "Displays all miscellaneous features", emoji = "✨"),
            nextcord.SelectOption(label = "Utility", description = "Displays all utility features", emoji = "🔨"),
            nextcord.SelectOption(label = "Management", description = "Displays all server management features", emoji = "👨‍🔧")
        ]
        super().__init__(placeholder='Select a category', min_values=1, max_values=1, options=selectOptions)

    async def callback(self, ctx):
        if self.values[0] == 'Management':
          embed = nextcord.Embed(title="Server Management Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``;slowmode <value_in_seconds>``",
                          value="Set the slowmode in seconds (e.g. .slowmode 3600)")
          embed.add_field(
              name=":warning: ``;txtnuke``",
              value=
              "Deletes all text channels\n**We recommend you do NOT perform this command.**"
          )
          embed.add_field(name="``;grename <new_name>``", value="Renames the guild")
          embed.add_field(name="``;massunban``", value="Unbans all members at once")
          embed.set_footer(
              icon_url=
              "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
              text="Norium Bot")
          await ctx.message.edit(embed=embed)
      
        if self.values[0] == 'Moderation':
          embed = nextcord.Embed(title="Moderation Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``;warn @<member> [reason]``", value="Warn a member")
          embed.add_field(name="``;mute @<member> [reason]``", value="Mute a member")
          embed.add_field(name="``;lock <reason>``",
                          value="Lock the current channel in which you are in")
          embed.add_field(name="``;ban @<member> [reason]``",
                          value="Ban a member from your server")
          embed.add_field(name="``;kick @<member> [reason]``",
                          value="Kick a member from your server")
          embed.add_field(
              name="``;unmute @<member>``",
              value="Unmute a member that was timed out",
                )
          embed.add_field(name="``;clear <msg_amount>``",
                          value="Clear several messages at once")
          embed.add_field(name="``;unban <user>#<discriminator>``",
                          value="Unban a member from your server")
          embed.add_field(name="``;unlock``", value="Unlock a channel")
          embed.add_field(name="``;moderate @<member>``",
                          value="Moderate a member's nickname")
          embed.add_field(name="``;warnings @[member]``",
                          value="View your or a certain user's warnings")
          embed.set_footer(
              icon_url=
              "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
              text="Norium Bot")
          await ctx.message.edit(embed=embed)


        if self.values[0] == 'Utility':
            embed = nextcord.Embed(title="Utility Plugin",
                           color=nextcord.Color.blurple())
            embed.add_field(name="``;poll <option_1> <option_2> <topic>``",
                    value="Send a voting message")
            embed.add_field(name="``;guildcount``",
                    value="Shows the amount of servers Norium Bot is in")
            embed.add_field(
                name="``;template``",
                value=
                "A basic rule template in case you don't have rules already or don't know what rules you should put"
            )
            embed.add_field(name="``;embed <text>``",
                    value="Send a custom embed message")
            embed.add_field(name="``;profile @[member]``",
                    value="Your's or another user's profile")
            embed.add_field(name="``;avatar @[member]``",
                    value="Displays your avatar or another member's avatar")
            embed.add_field(name="``;commandcount``", value="Overall command count")
            embed.add_field(
                name="``;stats``",
                value="Displays Norium Bot's CPU Time, Memory Usage and Uptime")
            embed.add_field(name="``;error [code]``", value="Look up some bot errors")
            embed.add_field(name="``;giveaway <duration> <prize>``",
                    value="Create a giveaway")
            embed.set_footer(
              icon_url=
              "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
              text="Norium Bot")
            await ctx.message.edit(embed=embed)

        if self.values[0] == 'Fun':
                embed = nextcord.Embed(title="Fun Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
                embed.add_field(name="``;bunger``", value="Bunger :hamburger:")
                embed.add_field(name="``;8ball <question>``",
                    value="Ask the almighty 8ball a question")
                embed.add_field(name="``;sus @[member]``", value="Sus-O-Meter :flushed:")
                embed.add_field(name="``;pp @[member]``", value="PP-O-Meter")
                embed.add_field(name="``;gayrate @[member]``",
                    value="See how gay you are or another member is")
                embed.add_field(name="``;kill @<member>``", value="Make someone unalive")
                embed.add_field(name="``;cat``", value="Sends random cat images")
                embed.add_field(name="``;dog``", value="Sends random dog images")
                embed.add_field(
                  name="``;simprate``",
                  value="See how much of a simp you are or another member is")
                embed.add_field(name="``;coinflip``", value="Flip a coin")
                embed.add_field(name="``;minecraft``",
                    value="Get a minecraft player's profile")
                embed.add_field(name="``;meme``", value="Sends a random meme")
                embed.set_footer(
                  icon_url=
                  "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
                  text="Norium Bot")
                await ctx.message.edit(embed=embed)

        if self.values[0] == 'Misc':
          embed = nextcord.Embed(title="Misc Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``;ping``", value="Shows client latency")
          embed.add_field(name="``;about``", value="Information about Norium Bot")
          embed.add_field(name="``;serverinfo``",
                          value="Information about the current guild")
          embed.add_field(name="``;links``", value="All Norium Bot related links")
          embed.add_field(name="``;version``",
                          value="The current version Norium Bot is on")
          embed.set_footer(
              icon_url=
              "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
              text="Norium Bot")
          await ctx.message.edit(embed=embed)

class HelpDropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDropdown())

@client.group(invoke_without_command=True)
async def help(ctx):
    support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
    docs = Button(label="Docs",
                  url="https://noriumbot-readthedocs.github.io/docs/")
    website = Button(label="Website", url="https://noriumbot.github.io/home/")

    view = HelpDropdownView()
    view.add_item(support)
    view.add_item(docs)
    view.add_item(website)

    embed = nextcord.Embed(title="Help Menu", color=nextcord.Color.blurple())
    embed.add_field(name="Moderation", value="``;help moderation``", inline = False)
    embed.add_field(name="Misc", value="``;help misc``", inline = False)
    embed.add_field(name="Utility", value="``;help utility``", inline = False)
    embed.add_field(name="Fun", value="``;help fun``", inline = False)
    embed.add_field(name="Server Management", value="``;help management``", inline = False)
    embed.add_field(name="**OR**", value="Choose something from the dropdown below.")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed, view=view)


@help.command()
async def moderation(ctx):
    embed = nextcord.Embed(title="Moderation Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``;warn @<member> [reason]``", value="Warn a member")
    embed.add_field(name="``;mute @<member> [reason]``", value="Mute a member")
    embed.add_field(name="``;lock <reason>``",
                    value="Lock the current channel in which you are in")
    embed.add_field(name="``;ban @<member> [reason]``",
                    value="Ban a member from your server")
    embed.add_field(name="``;kick @<member> [reason]``",
                    value="Kick a member from your server")
    embed.add_field(
        name="``;unmute @<member>``",
        value="Unmute a member that was timed out",
    )
    embed.add_field(name="``;clear <msg_amount>``",
                    value="Clear several messages at once")
    embed.add_field(name="``;unban <user>#<discriminator>``",
                    value="Unban a member from your server")
    embed.add_field(name="``;unlock``", value="Unlock a channel")
    embed.add_field(name="``;moderate @<member>``",
                    value="Moderate a member's nickname")
    embed.add_field(name="``;warnings @[member]``",
                    value="View your or a certain user's warnings")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@help.command()
async def misc(ctx):
    embed = nextcord.Embed(title="Misc Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``;ping``", value="Shows client latency")
    embed.add_field(name="``;about``", value="Information about Norium Bot")
    embed.add_field(name="``;serverinfo``",
                    value="Information about the current guild")
    embed.add_field(name="``;links``", value="All Norium Bot related links")
    embed.add_field(name="``;version``",
                    value="The current version Norium Bot is on")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    embed = nextcord.Embed(title="Fun Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``;bunger``", value="Bunger :hamburger:")
    embed.add_field(name="``;8ball <question>``",
                    value="Ask the almighty 8ball a question")
    embed.add_field(name="``;sus @[member]``", value="Sus-O-Meter :flushed:")
    embed.add_field(name="``;pp @[member]``", value="PP-O-Meter")
    embed.add_field(name="``;gayrate @[member]``",
                    value="See how gay you are or another member is")
    embed.add_field(name="``;kill @<member>``", value="Make someone unalive")
    embed.add_field(name="``;cat``", value="Sends random cat images")
    embed.add_field(name="``;dog``", value="Sends random dog images")
    embed.add_field(
        name="``;simprate``",
        value="See how much of a simp you are or another member is")
    embed.add_field(name="``;coinflip``", value="Flip a coin")
    embed.add_field(name="``;minecraft``",
                    value="Get a minecraft player's profile")
    embed.add_field(name="``;meme``", value="Sends a random meme")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@help.command()
async def management(ctx):
    embed = nextcord.Embed(title="Server Management Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``;slowmode <value_in_seconds>``",
                    value="Set the slowmode in seconds (e.g. .slowmode 3600)")
    embed.add_field(
        name=":warning: ``;txtnuke``",
        value=
        "Deletes all text channels\n**We recommend you do NOT perform this command.**"
    )
    embed.add_field(name="``;grename <new_name>``", value="Renames the guild")
    embed.add_field(name="``;massunban``", value="Unbans all members at once")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@help.command()
async def utility(ctx):
    embed = nextcord.Embed(title="Utility Plugin",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``;poll <option_1> <option_2> <topic>``",
                    value="Send a voting message")
    embed.add_field(name="``;guildcount``",
                    value="Shows the amount of servers Norium Bot is in")
    embed.add_field(
        name="``;template``",
        value=
        "A basic rule template in case you don't have rules already or don't know what rules you should put"
    )
    embed.add_field(name="``;embed <text>``",
                    value="Send a custom embed message")
    embed.add_field(name="``;profile @[member]``",
                    value="Your's or another user's profile")
    embed.add_field(name="``;avatar @[member]``",
                    value="Displays your avatar or another member's avatar")
    embed.add_field(name="``;commandcount``", value="Overall command count")
    embed.add_field(
        name="``;stats``",
        value="Displays Norium Bot's CPU Time, Memory Usage and Uptime")
    embed.add_field(name="``;error [code]``", value="Look up some bot errors")
    embed.add_field(name="``;giveaway <duration> <prize>``",
                    value="Create a giveaway")
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def txtnuke(ctx):
    embed = nextcord.Embed(
        title=":warning: Are you sure?",
        description=
        "All changes are irreversible, we are not responsible for any damage done to your server.",
        color=nextcord.Color.red())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")

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
    async def confirm(self, button: nextcord.ui.Button,
                      interaction: nextcord.Interaction):
        await interaction.response.send_message("Deleting channels...",
                                                ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button,
                     interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="Cancelling...",
                               description="Process cancelled.",
                               color=nextcord.Color.green())
        embed.set_footer(
            icon_url=
            "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
            text="Norium Bot")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.value = False
        self.stop()


@txtnuke.error
async def txtnuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
            title="No Permissions",
            description="You are missing the ``MANAGE_CHANNELS`` permission.",
            color=nextcord.Color.red())
        embed.set_footer(
            icon_url=
            "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
            text="Norium Bot")
        await ctx.send(embed=embed)


@client.command(aliases=["botinfo", "norium", "noriumbot", "info"])
async def about(ctx):
    embed = nextcord.Embed(
        title="About Norium Bot",
        description=
        "Norium Bot is a multi-purpose Discord Bot with features for everyone to access.",
        color=nextcord.Color.blue())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    embed.set_image(
        url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png"
    )
    await ctx.send(embed=embed)


@client.group(invoke_without_command=True, aliases=["errorcode", "ec", "code"])
async def error(ctx):
    embed = nextcord.Embed(title="Errors", color=nextcord.Color.red())
    embed.add_field(name="Unknown Command",
                    value="``;error unknown``",
                    inline=False)
    embed.add_field(name="No Permissions",
                    value="``;error permissions``",
                    inline=False)
    embed.add_field(name="Invalid Syntax",
                    value="``;error syntax``",
                    inline=False)
    embed.add_field(name="Member Not Found",
                    value="``;error member``",
                    inline=False)
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@error.command()
async def unknown(ctx):
    embed = nextcord.Embed(title="Unknown Command",
                           description="A command that cannot be found.",
                           color=nextcord.Color.red())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@error.command()
async def permissions(ctx):
    embed = nextcord.Embed(
        title="No Permissions",
        description="A command which you do not have permissions for.",
        color=nextcord.Color.red())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@error.command()
async def syntax(ctx):
    embed = nextcord.Embed(
        title="Invalid Syntax",
        description=
        "A command in which you did not include a required argument.",
        color=nextcord.Color.red())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@error.command()
async def member(ctx):
    embed = nextcord.Embed(
        title="Member Not Found",
        description="The member you mentioned doesn't exist.",
        color=nextcord.Color.red())
    embed.set_footer(
        icon_url=
        "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
        text="Norium Bot")
    await ctx.send(embed=embed)


@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

    memeData = json.load(memeAPI)

    memeURL = memeData['url']
    memeName = memeData['title']
    memePost = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed = nextcord.Embed(description=f"**[{memeName}]({memeLink})**",
                           color=nextcord.Color.blue())
    embed.set_image(url=memeURL)
    embed.set_footer(text=f"{memePost} on r/{memeSub}")
    await ctx.send(embed=embed) #credit: glowstik


client.run(token)