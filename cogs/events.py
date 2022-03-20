import nextcord
from nextcord.ext import commands

class Start(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    bot = f'<@!{self.client.user.id}>'
    if message.content == bot:
      await message.channel.send("My prefix is **;**")

  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(activity=nextcord.Activity(
        type=nextcord.ActivityType.listening, name=";help"))
    print(self.client.user.name + " is online!")

def setup(client):
  client.add_cog(Start(client))
