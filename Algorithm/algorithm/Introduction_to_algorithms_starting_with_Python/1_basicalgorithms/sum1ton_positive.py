# 1からnまでの総和を求める(nに正の整数値を読み込む)

print('1からnまでの総和を求める。')

while True:
    n = int(input('正の整数：'))
    if n > 0:
        break

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'1から{n}までの総和は{sum}です。')