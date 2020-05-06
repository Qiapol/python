# チェイン法を実現するハッシュクラスChainedHashの利用法

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['追加', '削除', '探索', 'ダンプ', '終了'])


def select_menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.追加:
        key = int(input('キー：'))
        val = input('値：')
        if not hash.add(key, val):
            print('追加失敗！')

    elif menu == Menu.削除:
        key = int(input('キー：'))
        if not hash.remove(key):
            print('削除失敗！')

    elif menu == Menu.探索:
        key = int(input('キー：'))
        t = hash.search(key)
        if t is not None:
            print(f'そのキーを持つ値は{t}です。')
        else:
            print('外套のデータは存在しません。')

    elif menu == Menu.ダンプ:
        hash.dump()

    else:
        break
