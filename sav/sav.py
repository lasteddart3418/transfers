import discord
from datetime import datetime
from discord.ext import commands


from core import checks
from core.models import PermissionLevel

options_menu="You have provided invalid dept code.\n\n`perks` - Perks Threads\n`giveaway ` - Giveaway Threads\n`scammer` - Scammer Report Threads\n`application` - Staff Application Threads\n`partnership`- Partnership Threads\n`owner` - Owner Threads\n"

DEPS_DATA = {
    "perks": {
        "category_id": 1222919013517099008 ,
        "pretty_name": "Perks Threads",
        "reminders": "None",
        "role_id": 1222579912615919666,
        "send_message_to_user": True
    },
    "giveaway": {
        "category_id": 1222920041826353152 ,
        "pretty_name": "Giveaway Threads",
        "reminders": "None",
        "role_id": 1222579912615919666,
        "send_message_to_user": True
    },
    "scammer": {
        "category_id": 1222920996823105648 ,
        "pretty_name": "Scammer Report Threads",
        "reminders": "None",
        "role_id": 1222579912615919666,
        "send_message_to_user": True
    },
    "application": {
        "category_id": 1223204766927032370 ,
        "pretty_name": "Staff Application Threads",
        "reminders": "None",
        "role_id": 1222579912615919666,
        "send_message_to_user": True
    },
        "partnership": {
        "category_id": 1223206926867894374 ,
        "pretty_name": "Partnership Threads",
        "reminders": "None",
        "role_id": 1222579912615919666,
        "send_message_to_user": True
    },
        "owner": {
        "category_id": 1276955415824961567 ,
        "pretty_name": "Owner Threads",
        "reminders": "None",
        "role_id": 1276957128908865546,
        "send_message_to_user": True
    },
}
class sav(commands.Cog, name="Sav Main Commands"):
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
            mes = "You are being transferred to **`"
            mes += data["pretty_name"]
            mes += "`**.\n"
            mes += "Please remain __patient__ while we find a suitable staff member to assist in your request.\n\n"
            
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
    await bot.add_cog(sav(bot))
