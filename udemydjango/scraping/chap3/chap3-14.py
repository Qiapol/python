import pandas as pd
import matplotlib.pyplot as plt

# グラフを表示する

# CSVファイルを読み込む
df = pd.read_csv('test.csv')
# 折れ線グラフを作成する
df.plot()
# 作ったグラフを表示する
plt.show()
