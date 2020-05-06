import pandas as pd
import matplotlib.pyplot as plt

# colorlistをリスト型で準備し、棒グラフの色を変化させる

# CSVファイルを読み込む(名前の列をインデックスで)
df = pd.read_csv('test.csv', index_col='名前')

# 棒グラフを作って画像ファイルを出力
colorlist = ['skyblue', 'steelblue', 'tomato', 'cadetblue', 'orange', 'sienna']
df.T.plot.bar(color=colorlist)
plt.legend(loc='lower right')
plt.show()
