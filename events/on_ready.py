from discord.ext import commands

class ReadyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected!')  # 起動時にメッセージを出力

def setup(bot):
    bot.add_cog(ReadyEvent(bot))  # Botにこのイベントを追加
    