import nextcord 
from nextcord.ext import commands 
import random 

class RollDice(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["rd", "dice", "roll"])
    async def rolldice(self, ctx):
        embed = nextcord.Embed(
            title = "Rolling the dice...",
            description = f"The dice was rolled and landed on **{random.randint(1, 6)}**!",
            color = nextcord.Color.random()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RollDice(client))