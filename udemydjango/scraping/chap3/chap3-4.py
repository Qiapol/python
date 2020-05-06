import pandas as pd

# 行データの追加

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 1行のデータを表示
print(f'C子のデータ\n { df.loc[2] }')

# 複数の行のデータを表示
print(f'C子とD郎のデータ\n { df.loc[[2, 3]] }')

# 指定した行の指定した列のデータを表示
print(f'C子の国語のデータ\n { df.loc[2]["国語"] }')
