a = int(input())
b = int(input())
c = int(input())
X = int(input())

count = 0
for i in range((X // 500) + 1):
    for j in range(((X - 500 * i) // 100) + 1):
        for k in range(((X - 500 * i - 100 * j) // 50) + 1):
            if X - (500 * i + 100 * j + 50 * k) == 0:
                count += 1
print(count)