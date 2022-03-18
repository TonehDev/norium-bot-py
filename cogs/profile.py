import nextcord
from nextcord.ext import commands
import asyncio

class UserInfo(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["ui", "user", "userinfo"])
  async def profile(self, ctx, member : nextcord.Member = None):
    if member == None:
      member = ctx.author

      
    message = await ctx.send("Loading user information...")
    await asyncio.sleep(0.5)
    await message.edit(f"Loaded")
    roles = [role for role in member.roles]

    embed = nextcord.Embed(title = f"{member.name}#{member.discriminator}'s Profile", color = member.color)
    embed.set_thumbnail(url = member.avatar.url)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
    embed.add_field(name = "ID", value = member.id)
    embed.add_field(name = "Nickname", value = member.display_name)
    embed.add_field(name = "Created at", value = member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "Joined at", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = f"Roles ({len(roles)})",  value = " ".join([role.mention for role in roles]))
    embed.add_field(name = "Top Role", value = member.top_role.mention)
    embed.add_field(name = "Is Bot", value = member.bot)
    embed.add_field(name = "Avatar URL", value = f"[Click Here]({member.avatar.url})")
    
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(UserInfo(client))