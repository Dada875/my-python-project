from discord.ext import commands

class HelloCommand(commands.Cog):
    """Helloコマンドを提供するCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        """ユーザーに挨拶します。"""
        await ctx.send('Hello!')

async def setup(bot):
    """Cogをセットアップします。"""
    await bot.add_cog(HelloCommand(bot))