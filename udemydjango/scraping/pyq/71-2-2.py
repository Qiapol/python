import csv
from io import StringIO

import requests

# 身長を格納するリスト
height_list = []
# 体重を格納するリスト
weight_list = []
# 年齢を格納するリスト
age_list = []

# URLからHTMLを取得します
url = "https://docs.pyq.jp/_static/assets/scraping/parse2.csv"
response = requests.get(url)
response.encoding = response.apparent_encoding

# CSVを解析
reader = csv.reader(StringIO(response.text))
print('-' * 10)
for row in reader:
    # 名前の取得と表示
    name = row[0]
    print(name)

    # 身長を保持する
    height_list.append(int(row[1]))
    # 体重を保持する
    weight_list.append(int(row[2]))
    # 年齢を保持する
    age_list.append(int(row[3]))

print('-' * 10)
# 平均身長を算出する
average_height = sum(height_list) / len(height_list)
print('平均身長:', average_height)

# 平均体重を算出する
average_weight = sum(weight_list) / len(weight_list)
print('平均体重:', average_weight)

# 平均年齢を算出する
average_age = sum(age_list) / len(age_list)
print('平均年齢:', average_age)
