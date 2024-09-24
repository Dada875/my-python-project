import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.logging_setup import setup_logging
from commands.api import call_chatgpt_api  # ChatGPT APIを呼び出す関数をインポート

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intentsを設定
intents = discord.Intents.default()
intents.message_content = True

# ログの設定を実行
logger = setup_logging()
logger.info('Bot is starting...')

# Botの初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# !ask コマンドでChatGPTに質問を投げる
@bot.command(name="ask")
async def ask_chatgpt(ctx, *, question):
    """ユーザーの質問をChatGPTに投げて、その応答を返す"""
    response = call_chatgpt_api(question)  # API呼び出し
    if response:
        await ctx.send(f" {response}")
    else:
        await ctx.send("ChatGPT APIからの応答に失敗しました。")

async def load_extensions():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    COMMANDS_DIR = os.path.join(BASE_DIR, 'commands')
    EVENTS_DIR = os.path.join(BASE_DIR, 'events')

    # commands ディレクトリ内のファイルを拡張としてロード
    for filename in os.listdir(COMMANDS_DIR):
        if filename.endswith('.py') and filename != '__init__.py' and filename != 'api.py':  # api.py を除外
            await bot.load_extension(f'commands.{filename[:-3]}')

    # events ディレクトリ内のファイルを拡張としてロード
    for filename in os.listdir(EVENTS_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'events.{filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
