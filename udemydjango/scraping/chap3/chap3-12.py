import pandas as pd

# 国語の点数でソート後、インデックスを削除したうえでCSVファイル出力

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# ソート(国語の点数が高いもの順)
kokugo = df.sort_values("国語", ascending=False)

# CSVファイルに出力する(インデックスを削除)
kokugo.to_csv('export2.csv', index=False)
