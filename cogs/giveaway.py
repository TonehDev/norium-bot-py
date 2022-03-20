import nextcord
from nextcord.ext import commands
import random
import asyncio

class Giveaway(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["giveaway", "create"])
  @commands.has_permissions(manage_messages = True)
  async def gcreate(self, ctx, time = None, *, prize = None):
    if time == None:
      embed = nextcord.Embed(
        title = "No Duration",
        description = "Please include a duration!",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)
    elif prize == None:
      embed = nextcord.Embed(
        title = "No Prize",
        description = "Please include a prize that you would like to give away!",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)
      
    embed = nextcord.Embed(
      title = "🎉 GIVEAWAY 🎉", 
      description = f"Prize: **{prize}**\nHost: {ctx.author.mention}\nEnds in: **{time}**", 
      color = nextcord.Color.blue()
    )

    time_convert = {"s":1, "m":60, "h":3600, "d": 86400}
    gawtime = int(time[0]) * time_convert[time[-1]]
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = f"Ends in {time}")
    gaw_msg = await ctx.send(embed=embed)

    await gaw_msg.add_reaction("🎉")
    await asyncio.sleep(gawtime)

    new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(self.client.user))

    winner = random.choice(users)

    embed = nextcord.Embed(title = "🎉 GIVEAWAY ENDED 🎉", description = f"Congratulations to {winner.mention} for winning the **{prize}**!", color = nextcord.Color.blue())
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
    await ctx.send(winner.mention, embed=embed)

  @gcreate.error
  async def gcreate_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_MESSAGES`` permission.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed) #credit: glowstik

def setup(client):
  client.add_cog(Giveaway(client))