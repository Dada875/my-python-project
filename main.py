import os
from dotenv import load_dotenv
from discord.ext import commands
from utils.logging_setup import setup_logging

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

# ログの設定を実行
logger = setup_logging()

logger.info('Bot is starting...')

# Botの実行
bot.run(TOKEN)
