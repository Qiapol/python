# 線形探索(番兵法)

from typing import Any, Sequence
import copy
import random


def seq_search(seq: Sequence, key: Any) -> int:
    """シーケンスseqからkeyと一致する要素を線形探索(番兵法)"""
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        # 必ず目的のキーは見つかるため、if文を1つ消去することができる
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


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