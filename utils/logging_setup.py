import logging

def setup_logging():
    # INFOレベルのログを設定
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Discordのライブラリ用のロガーを取得
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    # ファイルにログを保存したい場合は、以下を追加
    file_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    return logger
