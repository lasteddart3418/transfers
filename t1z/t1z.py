import discord
from datetime import datetime
from discord.ext import commands


from core import checks
from core.models import PermissionLevel

options_menu="You have provided invalid dept code.\n\n`mod` - Moderation Team\n`pt ` - Partnership Team\n`marketing` - Marketing Team\n`tl` - Team Leaders\n`hr`- Human Resources Team\n`management` - Management Team\n`exec` - Executive Team\n"

DEPS_DATA = {
        "mod": {
        "category_id": 1240756946110382221 ,
        "pretty_name": "Moderation Team",
        "reminders": "1. When reporting a member, please make sure to provide valid proof.
        2. Please make sure you check the report to ensure it breaks the rules before sending it.",
        "role_id": 1240758729213870190,
        "send_message_to_user": True
    },
        "pt": {
        "category_id": 1240756965307715604 ,
        "pretty_name": "Partnership Team",
        "reminders": "1. Please have your advertisement ready to send.
		2. Please make sure you meet our requirements.",
        "role_id": 1240758976509907065,
        "send_message_to_user": True
    },
        "marketing": {
        "category_id": 1240756983980752917 ,
        "pretty_name": "Marketing Team",
        "reminders": "None",
        "role_id": 1240761316973482129,
        "send_message_to_user": True
    },
        "tl": {
        "category_id": 1240757008567631922 ,
        "pretty_name": "Team Leaders",
        "reminders": "1. If you're looking to appeal an adwarn, please make sure you show a screenshot of the warning.
		2. Please make sure to provide a reason and counter proof for the appeal (such as your ad).",
        "role_id": 1240758458383597670,
        "send_message_to_user": True
    },
        "hr": {
        "category_id": 1240757032156401705 ,
        "pretty_name": "Human Resources Team",
        "reminders": " 1. If you're looking to report a staff member, please make sure to provide proof against this staff member.
		2. Please make sure to check your report to ensure it breaks the rules before sending it.",
        "role_id": 1240758274962358516,
        "send_message_to_user": True
    },
        "management": {
        "category_id": 1240757048891670559 ,
        "pretty_name": "Management Team",
        "reminders": "1. If you're looking to Affiliate with us, please make sure to copy a __Permanent__ invite and post it into your Affiliation channel.
		2. Please make sure the invite is permanent before sending your invite.",
        "role_id": 1240758110264623146,
        "send_message_to_user": True
    },
        "exec": {
        "category_id": 1240757072644018308 ,
        "pretty_name": "Executive Team",
        "reminders": "None",
        "role_id": 1240757896330084473,
        "send_message_to_user": True
    },
}
class tom(commands.Cog, name="Tom Main Commands"):
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
    await bot.add_cog(tom(bot))
