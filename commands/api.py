import os
import requests
import openai
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# APIキーが正しく読み込まれているか確認
print(OPENAI_API_KEY)  # None でないことを確認

def call_chatgpt_api(prompt):
    """ChatGPT APIを呼び出して、プロンプトに対する応答を取得する関数"""
    url = "https://api.openai.com/v1/chat/completions"  # 修正：正しいエンドポイント
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # 使用するモデル
        "messages": [{"role": "user", "content": prompt}],  # チャット形式のメッセージ
        "max_tokens": 100,  # 最大トークン数
        "temperature": 0.7  # 応答のランダム性（0.0から1.0）
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # HTTPステータスコードをチェック
        result = response.json()
        return result['choices'][0]['message']['content'].strip()  # チャット形式の応答
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTPエラーが発生しました: {http_err}")
        print(f"レスポンス内容: {response.text}")  # エラー時のレスポンスの内容を表示
    except requests.exceptions.RequestException as e:
        print(f"APIリクエストに失敗しました: {e}")
        return None

# テスト: プロンプトに対する応答を確認
response = call_chatgpt_api("こんにちは、元気ですか？")
if response:
    print(f"ChatGPTの応答: {response}")
else:
    print("ChatGPT APIからの応答に失敗しました。")
