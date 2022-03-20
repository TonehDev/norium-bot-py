import nextcord  
from nextcord.ext import commands
from nextcord.ui import Button, View

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["inv"])
    async def invite(self, ctx):
        support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
        invite = Button(label="Invite Norium",
                  url="https://dsc.gg/noriumv3")

        view = View()
        view.add_item(support)
        view.add_item(invite)

        embed = nextcord.Embed(
            title = "Invite Norium Bot",
            description = "Invite Norium Today - Simply click the buttons below and you're done.",
            color = nextcord.Color.blurple()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/943924201688027206/955039552333053973/unknown.png", text = "Norium Bot")
        await ctx.send(embed=embed, view=view)


def setup(client):
    client.add_cog(Invite(client))