import nextcord
from nextcord.ext import commands

class Clear(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["purge"])
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=2):
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)

  # Error Handling

  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``;clear <msg_amount>``", inline = False)
      embed.add_field(name = "Example", value = "``;clear 5``", inline = False)
      embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
      await ctx.send(embed=embed) #credit: lucas

def setup(client):
    client.add_cog(Clear(client))