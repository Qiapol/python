# ミュータブルなシーケンスの要素の並びを反転

import random
from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    """ミュータブルなシーケンスaの要素の並びを反転"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    print('配列の要素の並びを反転します。')

    while True:
        n = int(input('要素数：'))
        if n > 0:
            break
        print('要素数は正の数を記載すること')

    a = [None] * n

    for i in range(n):
        a[i] = random.randint(1, 100)

    print(f'反転前：{a}')

    reverse_array(a)

    print('要素の並びを反転しました。')
    print(f'反転後：{a}')