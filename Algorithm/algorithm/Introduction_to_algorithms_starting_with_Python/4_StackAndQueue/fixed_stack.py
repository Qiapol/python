# 固定長スタッククラス

from typing import Any

class FixedStack:
    """固定長スタッククラス"""

    class Empty(Exception):
        """空のFixedStackに対してpopあるいはpeekが呼び出されたときに送出する例外"""
        pass  # 本来はここに例外処理を記載。今はデータ構造とは関係ないため握りつぶす。

    class Full(Exception):
        """満杯のFixedStackに対してpushが呼び出されたときに送出する例外"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """初期化"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """スタックに積まれているデータ数を返す"""
        return self.ptr

    def is_empty(self) -> bool:
        """スタックは空であるか"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """スタックは満杯か"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """スタックにvalueをプッシュ"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """スタックからデータをポップ(頂上のデータを取り出す)"""
        if self.is_empty():
            raise FixedStack.Empty
        # ポインタを動かすことで論理削除が行われている
        self.ptr -= 1
        return self.stk[self.ptr]

    def peak(self) -> Any:
        """スタックからデータをピーク(頂上のデータをのぞき見)"""
        if self.is_empty():
            raise FixedStack.Empty
        # ポインタは動かないため、データの論理上の消去は行われない
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """スタックを空にする(全データの削除)"""
        # ポインタを0に持っていくことで、論理的に全データの消去が行われている
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """スタックからvalueを探して添字(見つからなければ-1)を探す"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        """スタックに含まれるvalueの個数を返す"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """スタックにvalueは含まれているか"""
        # A in B(BにAが含まれているか) の判定文を使用することができる
        return self.count(value)

    def dump(self):
        """ダンプ(スタック内の全データを底->頂上の順に表示)"""
        if self.is_empty():
            print('スタックは空です。')
        else:
            print(self.stk[:self.ptr])