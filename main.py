import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.logging_setup import setup_logging

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intentsを設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージコンテンツのIntentを有効化

# ログの設定を実行
logger = setup_logging()
logger.info('Bot is starting...')

# Botの初期化
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    COMMANDS_DIR = os.path.join(BASE_DIR, 'commands')
    EVENTS_DIR = os.path.join(BASE_DIR, 'events')

    print(f"BASE_DIR: {BASE_DIR}")
    print(f"COMMANDS_DIR: {COMMANDS_DIR}")
    print(f"EVENTS_DIR: {EVENTS_DIR}")

    # コマンドをロード
    for filename in os.listdir(COMMANDS_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'commands.{filename[:-3]}')

    # イベントをロード
    for filename in os.listdir(EVENTS_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'events.{filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
