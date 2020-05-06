# 自分の答え
s = input()
count = 0
for i in range(len(s)):
    if s[i] == '1':
        count += 1
print(count)

# 最速の答え
print(input().count('1'))