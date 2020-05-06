import json

# 辞書型 -> JSON

# 辞書を生成
kenji = {
    "id": 1,
    "name": "古村賢治",
    "age": 38,
}

# 辞書をJSON形式の文字列に変換
out = json.dumps(kenji)

# 出力
print(out)
print(type(out))