import logging

def setup_logging():
    """ロギングの設定を行います。"""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    return logger

async def load_extensions():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    COMMANDS_DIR = os.path.join(BASE_DIR, 'commands')
    EVENTS_DIR = os.path.join(BASE_DIR, 'events')

    print(f"BASE_DIR: {BASE_DIR}")
    print(f"COMMANDS_DIR: {COMMANDS_DIR}")
    print(f"EVENTS_DIR: {EVENTS_DIR}")

    # 以下省略
