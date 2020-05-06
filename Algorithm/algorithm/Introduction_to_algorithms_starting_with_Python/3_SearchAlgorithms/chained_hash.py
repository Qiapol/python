# チェイン法によるハッシュ

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """ハッシュを構成するノード"""
    def __init__(self, key: Any, value: Any, next: None) -> None:
        """初期化"""
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """チェイン法を実現するハッシュクラス"""
    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """キーkeyを持つ要素の探索(値を返却)"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """キーがkeyで値がvalueの要素の追加"""
        hash = self.hash_value(key)
        p = self.table[hash]

        # 線形リストの中でkey値が重複しないかの調査
        while p is not None:
            if p.key == key:
                return False
            p = p.next

        # 重複しなければ、線形リストの「先頭」に挿入する
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        """キーkeyを持つ要素の削除"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None  # 前回の着目ノード

        while p is not None:
            if p.key == key:
                # 線形リストの先頭ノード
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """ハッシュ表をダンプ"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')
                p = p.next
            print()
