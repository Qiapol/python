# 単純交換ソート
import random
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート(第3版：走査範囲を限定)"""


    # 下のコードは無限ループする
    # while n >= 1:
    #     for i in range(n - 1):
    #         if a[i] > a[i + 1]:
    #             a[i], a[i + 1] = a[i + 1], a[i]
    #             last = i
    #     n = last

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
