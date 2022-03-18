import nextcord
from nextcord.ext import commands

class Poll(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def poll(self, ctx, *, choice1, choice2, topic):
    embed = nextcord.Embed(
      title = topic,
      description = f":one: {choice1}\n:two: {choice2}",
      color = nextcord.Color.random()
    )
    embed.set_footer(text = f"Asked by {ctx.author.name}#{ctx.author.discriminator}")
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")

  # Error Handling
  @poll.error
  async def poll_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;poll <option_1> <option_2> <vote>``", inline = False)
      embed.add_field(name = "Example", value = "``;poll Cats Dogs Which one of these do you prefer?``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Poll(client))