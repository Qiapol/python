import math

# 縦横が整数で面積がareaの長方形の辺の長さを列挙

area = int(input('面積は：'))

for i in range(1, int(math.sqrt(area) + 1)):
    if area % i:
        continue
    print(f'{i}×{area // i}')