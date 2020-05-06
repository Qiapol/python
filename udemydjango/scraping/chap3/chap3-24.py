import pandas as pd
import openpyxl

# Excelファイルを読み込む(複数シートを読み込む -> sheet_nameを指定するだけ)
df = pd.read_excel('csv_to_excel3.xlsx')
print(df)
df = pd.read_excel('csv_to_excel3.xlsx', sheet_name='国語でソート')
print(df)
