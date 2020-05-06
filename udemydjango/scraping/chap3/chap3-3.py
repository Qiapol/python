import pandas as pd

# 列データの追加

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 1列のデータを表示
print(f'国語の列データ\n { df["国語"]}')

# 複数列のデータを表示
print(f'国語と数学の列データ\n { df[["国語", "数学"]] }')
