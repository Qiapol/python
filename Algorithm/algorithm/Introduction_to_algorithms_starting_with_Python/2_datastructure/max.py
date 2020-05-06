import random
from typing import Any, Sequence

# シーケンスの要素の最大値を表示する


def max_of(a: Sequence) -> Any:
    """シーケンスaの要素の最大値を返却する"""
    maximum = a[0]
    for i in range(1, len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print('配列の最大値を求めます。')

    while True:
        # 数値以外を入れると実行時エラーでプログラム中断
        num = int(input('要素数：'))
        if num > 0:
            break
        print('1以上の数値を入力してください')

    x = [None] * num  # 要素数numのリストを生成

    for i in range(num):
        x[i] = random.randint(1, 1000)

    print(x)
    print(f'最大値は{max_of(x)}です。')