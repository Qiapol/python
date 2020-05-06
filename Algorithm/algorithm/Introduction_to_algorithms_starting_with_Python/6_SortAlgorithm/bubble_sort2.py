# 単純交換ソート
import random
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート(第2版：交換回数による打切り)"""
    n = len(a)
    for i in range(n - 1):
        exchange_count = 0
        for j in range(n - i - 1):
            if j[i] > j[i + 1]:
                j[i], j[i + 1] = a[j + 1], a[j]
                exchange_count += 1
        # バブルソートで交換回数が0回 = すでにソート済なのでソート処理を打切り
        if exchange_count == 0:
            break


if __name__ == '__main__':
    print('単純交換ソート(バブルソート)')
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(1, 100)

    print(x)
    bubble_sort(x)

    print('昇順にソートしました。')
    print(x)