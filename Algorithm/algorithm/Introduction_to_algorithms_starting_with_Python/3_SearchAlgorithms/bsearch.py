# ２分探索
from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyに一致する要素を2分探索する。"""
    pl = 0
    pr = len(a) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
    return -1


if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num

    x[0] = int(input('x[0]：'))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('探す値：'))

    idx = bin_search(x, ky)

    if idx == -1:
        print('その値の要素は存在しません。')
    else:
        print(f'それはx[{idx}]にあります。')