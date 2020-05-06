# 3つの整数値を読み込んで最大値を求めて表示

print('3つの整数値の最大値を求めます。')
a = int(input('正の整数a:'))
b = int(input('正の整数b:'))
c = int(input('正の整数c:'))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f'最大値は{maximum}です。')