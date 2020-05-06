import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルを読み込む(名前の列をインデックスで)
df = pd.read_csv('test.csv', index_col='名前')

# 棒グラフを作って画像ファイルを出力する
df.T.plot.bar()
plt.legend(loc='lower right')
plt.show()
