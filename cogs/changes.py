import nextcord
from nextcord.ext import commands

class Changes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.is_owner()
  @commands.has_permissions(manage_channels = True)
  async def quickfix(self, ctx, *, message):
    embed = nextcord.Embed(
      title = "Quickfixes", 
       description = f"{message}", 
      color = nextcord.Color.magenta()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    await ctx.reply.send(embed=embed)
    await ctx.message.delete()

  @commands.command(aliases=["rt"])
  async def template(self, ctx):
    embed = nextcord.Embed(
      title = "Guidelines", 
      description = "Please read these rules thoroughly before you start chatting.", 
      color = nextcord.Color.random()
    )
    embed.add_field(name = "1# No discrimination", value = "``Discrimination`` including racism, homophobia, sexism, ableism etc.\nWe respect every member on this server no matter what sexuality, race and other they are.", inline = False)
    embed.add_field(name = "2# Toxicity", value = "Please avoid ``Toxicity`` as much as you can.\nIf you see a member being toxic towards somebody else, report them to staff!", inline = False)
    embed.add_field(name = "3# Inappropriate Discussions", value = "``Religious, NSFW and Political`` chat topics are not tolerated.\nThis is supposed to be a clean community server so keep that stuff out of here!", inline = False)
    embed.add_field(name = "4# Privacy", value = "``Hacking, DDOSing, Doxxing etc.`` are something that should not be allowed in general.\nEvery member's privacy deserves to be respected. ", inline = False)
    embed.add_field(name = "5# Direct Messages", value = "``Advertisements, Threats etc.`` do not belong in other member's direct messages.\nIf you see anything suspicious in your DMs, make sure to report that to the staff!", inline = False)
    embed.add_field(name = "6# Posts", value = "``Gore, Nudes, NSFW generally`` are not allowed in this server.\nPlease make sure to report these kinds of people to staff!", inline = False)
    embed.add_field(name = "7# Loopholes", value = "``People who find loopholes`` will be banned without hesitation.\nMake sure to report these people aswell.", inline = False)
    embed.add_field(name = "8# Common Sense", value = "Please ``use your mind`` as we cannot state every rule.", inline = False)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await ctx.message.delete()

  @commands.command()
  @commands.is_owner()
  @commands.has_permissions(manage_channels = True)
  async def change(self, ctx, *, message):
    embed = nextcord.Embed(
      title = "Quick Changes", 
       description = f"{message}", 
      color = nextcord.Color.magenta()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)
    await ctx.message.delete()

  @commands.command()
  @commands.is_owner()
  @commands.has_permissions(manage_channels = True)
  async def announce(self, ctx, *, message):
    embed = nextcord.Embed(
      title = "Announcement", 
      description = f"{message}", 
      color = nextcord.Color.random()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)
    await ctx.message.delete()
  
  @commands.command()
  @commands.is_owner()
  @commands.has_permissions(manage_channels = True)
  async def changelog(self, ctx, *, message):
    embed = nextcord.Embed(
      title = "New Update", 
      description = f"{message}", 
      color = nextcord.Color.green()
    )
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed)
    await ctx.message.delete()

def setup(client):
  client.add_cog(Changes(client))