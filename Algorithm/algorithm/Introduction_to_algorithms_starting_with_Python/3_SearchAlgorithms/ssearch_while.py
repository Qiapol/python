# 線形探索（while文）
import random
from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素の線形探索(while文)"""
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(1, 100)

    print(f'シーケンス：{x}')

    ky = int(input('探す値：'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('その値の要素は存在しません。')
    else:
        print(f'それはx[{idx}]にあります。')