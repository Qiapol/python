import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 表データの情報を表示
print(f'データの件数：{ len(df) }')
print(f'項目名：{ df.columns.values }')
print(f'インデックス：{ df.index.values }')