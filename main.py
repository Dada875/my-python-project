import os
from dotenv import load_dotenv
from discord.ext import commands

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Botのインスタンスを作成
bot = commands.Bot(command_prefix="!")

# コマンドをロード
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# イベントをロード
for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')

# Botの実行
bot.run(TOKEN)
