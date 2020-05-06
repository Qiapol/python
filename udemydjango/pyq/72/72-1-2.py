import json

# JSON形式の文字列を定義
items_str_as_json = '[{"id": 1, "name": "りんご"}, {"id": 2, "name": "オレンジ"}]'


# JSON形式の文字列をPythonの型（リスト）に変換
sales_list = json.loads(items_str_as_json)


# 変換した結果を出力
for sales in sales_list:
    print(f'{sales["id"]} - {sales["name"]}')