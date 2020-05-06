# 単純交換ソート
import random
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート"""
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


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