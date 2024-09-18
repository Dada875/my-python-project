import requests

def get_data():
    """APIを呼び出してデータを取得する関数"""
    try:
        response = requests.get('https://api.example.com/data')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"APIリクエストに失敗しました: {e}")
        return None
