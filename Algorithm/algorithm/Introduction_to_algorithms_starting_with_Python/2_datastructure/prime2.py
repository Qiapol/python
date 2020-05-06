# 1,000以下の素数を列挙(第２版)

counter = 0
prime = [None] * 500
ptr = 0

prime[ptr] = 2
ptr += 1

for i in range(3, 1001, 2):
    for j in range(1, ptr):
        counter += 1
        if i % prime[j] == 0:
            break
    else:
        prime[ptr] = i
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'除算を行った回数：{counter}回')
