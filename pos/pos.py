import discord
from datetime import datetime
from discord.ext import commands


from core import checks
from core.models import PermissionLevel

options_menu="You have provided invalid dept code.\n\n`general` - General Support\n`pr` - PR Support\n`pos` - AdvancePOS Support\n"

DEPS_DATA = {
    "general": {
        "category_id": 1297495563390160919 ,
        "pretty_name": "General Support,",
        "reminders": "None",
        "role_id": 1249750181243519097,
        "send_message_to_user": True
    },
    "pr": {
        "category_id": 1297567285493633115 ,
        "pretty_name": "PR Support",
        "reminders": "None",
        "role_id": 1269697972535562300,
        "send_message_to_user": True
    },
    "pos": {
        "category_id": 1297567756320772157 ,
        "pretty_name": "AdvancePOS Support",
        "reminders": "None",
        "role_id": 1269698132820758582,
        "send_message_to_user": True
   },
}
class pos(commands.Cog, name="pos"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def transfer(self, ctx, *, to: str=None):
        """Command that transfers thread to other departments."""
        if to is None:
            embed = discord.Embed(title=f"Department Transfer", description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            return await ctx.send(embed=embed)
        to = to.lower()
        data = None
        try:
            data = DEPS_DATA[to]
        except:
            embed = discord.Embed(title=f"Department Transfer",description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
            return

        if data["send_message_to_user"]:
            mes = "You have now been transferred to the **`"
            mes += data["pretty_name"]
            mes += "department"
            mes += "`**.\n"
            mes += "Please explain your __inquiries/problems__ in detail for faster support. \n"
            mes += "You will be transferred to another department if deemed necessary.\n\n"
            
            if data["reminders"] is not None:
                mes += "**__Reminders__**\n"
                mes += data["reminders"]

            msg = ctx.message
            msg.content = mes
            
            await ctx.thread.reply(msg, anonymous = False)
        
        await ctx.channel.edit(category=self.bot.get_channel(data["category_id"]), sync_permissions=True) 
        await ctx.send("<@&%s>" % str(data["role_id"]))

    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def stransfer(self, ctx, to: str=None):
        """Silently transfers thread"""
        if to is None:
            embed = discord.Embed(title=f"Silent Transfer", description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            return await ctx.send(embed=embed)
        to = to.lower()
        data = None
        try:
            data = DEPS_DATA[to]
        except:
            embed = discord.Embed(title=f"Silent Transfer",description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
            return

        await ctx.channel.edit(category=self.bot.get_channel(data["category_id"]), sync_permissions=True) 
        await ctx.send("Silent Transfer - <@&%s>" % str(data["role_id"]))

    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def id(self, ctx):
        await ctx.send(ctx.thread.id)

async def setup(bot):
    await bot.add_cog(pos(bot))
