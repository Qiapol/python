# 3つの整数値の最大値を求めて表示（全ての大小関係に対して確認）

def max3(a, b, c):
    """a, b, cの最大値を求めて返却"""
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum