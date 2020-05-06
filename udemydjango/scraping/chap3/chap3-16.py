import pandas as pd
import matplotlib.pyplot as plt

# index_col -> indexとするcolumn名
# CSVファイルを読み込む
df = pd.read_csv('test.csv', index_col='名前')
print(df)

# 国語の棒グラフを作って表示する
df['国語'].plot.barh()
plt.legend(loc='lower left')
plt.show()

# 国語と数学の棒グラフを作って表示する
df[['国語', '数学']].plot.barh()
plt.legend(loc='lower left')
plt.show()

# C子の棒グラフを作って表示する
df.loc['C子'].plot.barh()
plt.legend(loc='lower left')
plt.show()

# C子の円グラフを作って表示する
df.loc['C子'].plot.pie(labeldistance=0.6)
plt.legend(loc='lower left')
plt.show()
