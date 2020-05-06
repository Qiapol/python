import json

# 辞書を生成
fruits = [
    {"name": "オレンジ", "price": 120},
    {"name": "グレープフルーツ", "price": 200},
]

# 辞書をJSON形式の文字列に変換
fruits_as_json = json.dumps(fruits)

# 出力
print(fruits_as_json)
