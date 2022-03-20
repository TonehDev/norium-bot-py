import nextcord
from nextcord.ext import commands
import asyncio

class ServerInfo(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["si", "gi", "guildinfo"])
  async def serverinfo(self, ctx):
    message = await ctx.send("Loading server information...")
    await asyncio.sleep(0.5)
    await message.edit(f"Loaded")
    role_count = len(ctx.guild.roles)
    bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    embed = nextcord.Embed(title = f"Information for **{ctx.guild.name}**", color = nextcord.Color.blue())
    embed.add_field(name = "Guild Name", value = f"``{ctx.guild.name}``")
    embed.add_field(name = "Members", value = f"``{ctx.guild.member_count}``")
    embed.add_field(name = "Verification Level", value = f"``{str(ctx.guild.verification_level)}``")
    embed.add_field(name = "Highest Role", value = f"``{ctx.guild.roles[-2]}``")
    embed.add_field(name = "Role Count", value = f"``{str(role_count)}``")
    embed.add_field(name = "Bots", value = ', '.join(bots))
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(embed=embed) 
def setup(client):
  client.add_cog(ServerInfo(client))