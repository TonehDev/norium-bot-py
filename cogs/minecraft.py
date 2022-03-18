import nextcord
from nextcord.ext import commands
import asyncio

class getMinecraftInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["mc", "mcprofile", "mcuser"])
    async def minecraft(self, ctx, *, name):
        message = await ctx.send("Loading Minecraft profile...")
        await asyncio.sleep(0.5)
        await message.edit(f"Loaded")
        url = "https://tr.namemc.com/profile/{}".format(name)
        embed = nextcord.Embed(
            title=f"Minecraft Profile for {name}",
            description=f"[NameMC Profile]({url})",
            colour=nextcord.Colour.gold()
        )
        embed.add_field(name = "Skull Command (1.13+)",value='``/give @p minecraft:player_head{p1}SkullOwner:"{name}"{p2}'.format(p1="{",name=name,p2="}``"),inline=False)
        embed.add_field(name = "Skull Command (1.13-)",value='``/give @p minecraft:skull 1 3 {p1}SkullOwner:"{name}"{p2}'.format(p1="{",name=name,p2="}``"),inline=False)
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/947123850305495091/947394665609564249/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

    # Error Handling

    @minecraft.error
    async def minecraft_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
        )
        embed.add_field(name = "Usage", value = "``;minecraft <player>``", inline = False)
        embed.add_field(name = "Example", value = "``;minecraft Notch``", inline = False)
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"{ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(getMinecraftInfo(bot))