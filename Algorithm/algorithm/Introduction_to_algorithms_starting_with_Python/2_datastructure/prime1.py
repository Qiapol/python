# 1,000以下の素数を列挙(第1版)

counter = 0

for i in range(2, 1001):
    for j in range(2, i):
        counter += 1
        if i % j == 0:
            break
    else:
        print(i)

print(f'除算を行った回数：{counter}回')