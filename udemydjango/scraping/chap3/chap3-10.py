import pandas as pd

# 行と列を入れ替える

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 行と列を入れ替える
print(f'行と列を入れ替える\n {df.T}')

# データをリスト化する
print(f'Pythonのリストデータ化\n {df.values}')
