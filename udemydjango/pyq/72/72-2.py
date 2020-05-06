import requests
import json

# APIを呼び出し結果（Response)を受け取ります
res = requests.get('https://docs.pyq.jp/_static/assets/web_api/json/data/items.json')

# レスポンスの結果をjson形式の文字列として解析します
items = json.loads(res.text)

# 解析した結果（リスト）を出力します
for item in items:
    print(f'{item["name"]}:{item["stock"]}')
