import os
import discord  # discord.py ライブラリをインポート
from dotenv import load_dotenv
from discord.ext import commands
from utils.logging_setup import setup_logging

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intentsを設定
intents = discord.Intents.default()
intents.messages = True  # メッセージ関連のイベントを受け取るために有効化

# Botの初期化
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

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
