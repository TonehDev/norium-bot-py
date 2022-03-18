import nextcord
from nextcord.ext import commands
import random

class Kill(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def kill(self, ctx, *, member : nextcord.Member):
      way = [
      f"hugged {member.mention} to death",
      f"poisoned {member.mention}",
      f"pushed {member.mention} off a cliff",
      f"spawned a zombie which killed {member.mention}",
      f"pushed {member.mention} on a railway",
      f"set {member.mention} on fire",
      f"held {member.mention}'s underwater for 10 days straight",
      f"threw a bunch of knives at {member.mention}",
      f"boxed {member.mention} to death",
      f"sent too much cringe posts until {member.mention} died",
      f"removed {member.mention}'s brain",
      f"destroyed {member.mention}'s braincells",
      f"slapped {member.mention} to South Africa",
      f"kept {member.mention} in their basement for 50 years",
      f"sent Gordon Ramsay to {member.mention} so he can insult them to death",
      f"acquired the Infinity Gauntlet and snapped {member.mention} away",
      f"sent the Man behind the slaughter to {member.mention}",
      f"was too cringe for {member.mention}",
      f"just gave an electric shock to {member.mention}",
      f"punched {member.mention} using their crocs",
      f"literally fed plastic to {member.mention}",
      f"cancelled {member.mention}",
      f"killed {member.mention} using a turtle",
    ]
      embed = nextcord.Embed(
        title = f"Kill",
        description = f"{ctx.author.mention} {random.choice(way)}",
        color = nextcord.Color.random()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

  # Error Handling
  
  @kill.error
  async def kill_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):
      embed = nextcord.Embed(
        title = "Member Not Found",
        description = f"No member named ``{ctx.member.name}#{ctx.member.discriminator}`` found.",
        color = nextcord.Color.red()
      )
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)
  

def setup(client):
  client.add_cog(Kill(client))