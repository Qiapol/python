import json

# JSON形式の文字列を定義
person_str_as_json = '{"id": 101, "name": "古村健太郎", "age": 38}'

# JSON形式の文字列をPythonの型（リスト）に変換
person = json.loads(person_str_as_json)

# 表示
print(f'{person["name"]} {person["age"]}歳')
