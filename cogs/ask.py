import nextcord
from nextcord.ext import commands
import random


class Ask(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball", "ask"])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", "Outlook not so good.",
            "Very doubtful."
        ]
        embed = nextcord.Embed(title="🎱 8ball says...",
                               color=nextcord.Color.random())
        embed.add_field(name="Question", value=f"{question}", inline="false")
        embed.add_field(name="Answer",
                        value=f"{random.choice(responses)}",
                        inline="false")
        embed.set_footer(
            icon_url=
            "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png",
            text="Norium Bot")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/948235933709373470/948606008937312336/Webp.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ask(client))
