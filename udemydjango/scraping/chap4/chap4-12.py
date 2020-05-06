import pandas as pd
import matplotlib.pyplot as plt

# データフレームを読み込む
df = pd.read_csv('AveTemp_TOKYO.csv', index_col='時点')

# 平均気温で折れ線グラフを表示
df['年平均気温【℃】'].plot()
plt.show()
