from discord.ext import commands

class ReadyEvent(commands.Cog):
    """Botが起動したときのイベントを処理するCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Botが起動したときに呼び出されます。"""
        print(f'{self.bot.user} has connected!')

async def setup(bot):
    """Cogをセットアップします。"""
    await bot.add_cog(ReadyEvent(bot))