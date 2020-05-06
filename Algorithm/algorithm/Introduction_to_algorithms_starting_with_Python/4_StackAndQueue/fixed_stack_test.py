# 固定長スタックFixedStackの利用例

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['プッシュ', 'ポップ', 'ピーク', '探索', 'ダンプ', '終了'])


def select_menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(64)

while True:
    print(f'現在のデータ数：{len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.プッシュ:
        x = int(input('データ：'))
        try:
            s.push(x)
        except FixedStack.Full:
            print('スタックが満杯です。')

    elif menu == Menu.ポップ:
        try:
            x = s.pop()
            print(f'ポップしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')

    elif menu == Menu.ピーク:
        try:
            x = s.peak()
            print(f'ピークしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')

    elif menu == Menu.探索:
        x = int(input('値：'))
        if x in s:
            print(f'{s.count(x)}個含まれ、先頭の位置は{s.find(x)}です。')
        else:
            print('その値は含まれません。')

    elif menu == Menu.ダンプ:
        s.dump()

    else:
        break
