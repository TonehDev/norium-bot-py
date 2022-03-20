import nextcord
from nextcord.ext import commands 
import random

class CoinFlip(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["cf", "flip", "coin"])
    async def coinflip(self, ctx):
        sides = [
            "Tails",
            "Heads"
        ]
        embed = nextcord.Embed(
          title = "Coin flipped",
          description = f"The coin landed on **{random.choice(sides)}**!",
          color = nextcord.Color.random()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CoinFlip(client))