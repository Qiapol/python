import pandas as pd

# 列データ、行データを削除する

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 「名前」の列を削除
print(f'「名前」の列を削除\n {df.drop("名前", axis=1)}')

# インデックス2の行を削除
print(f'インデックス2の行を削除\n {df.drop(2, axis=0)}')

print('---------------------------------------------')
# df.drop(axis)
# axis=0 : index, axis=1 : columns
