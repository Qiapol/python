# 自分の答え
# n = input()
# l = list(map(int, input().split()))
#
# count = 0
# flag = True
#
# while flag:
#     for i in range(len(l)):
#         if l[i] % 2 == 1:
#             flag = False
#             break
#     count += 1
#     l = list(map(lambda x: x // 2, l))
# print(count)

# 人の答え
input()
A = list(map(int, input().split()))

count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)
