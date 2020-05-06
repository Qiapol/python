import pandas as pd

# 国語の点数でソート後、インデックス/ヘッダーを削除したうえでファイル出力

# CSVファイルに読み込む
df = pd.read_csv('test.csv')

# ソート(国語の点数が高いもの順)
kokugo = df.sort_values('国語', ascending=False)

# CSVファイルに出力する(インデックス、ヘッダー削除)
kokugo.to_csv('export3.csv', index=False, header=False)
