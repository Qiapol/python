import requests
import json
from datetime import datetime

# APIを呼び出し結果（Response)を受け取ります
res = requests.get('https://docs.pyq.jp/_static/assets/web_api/json/data/sales_daily.json')

# レスポンスの結果をjson形式の文字列として解析します
sales_list = json.loads(res.text)

# 解析した結果（リスト）を出力します
for sales in sales_list:
    sale_day = datetime.strptime(sales["day"], "%Y/%m/%d").date()
    print(f'{sale_day:%m/%d} - {sales["num"]}個')
