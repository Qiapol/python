import pandas as pd

# 国語の点数でソート後、CSVファイルに出力する(インデックス込)

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# ソート(国語の点数が高いもの順)
kokugo = df.sort_values("国語", ascending=False)

# CSVファイルに出力する
kokugo.to_csv('export1.csv')
