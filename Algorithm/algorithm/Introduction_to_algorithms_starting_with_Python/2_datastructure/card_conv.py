# 読み込んだ10進整数を2進数～36進数へと基数変換して表示


def card_conv(x: int, r: int) -> str:
    """整数値xをr進法に変換した数値を表す文字列を返却"""

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10進数を基数変換します。')

    while True:
        # 整数値xを読み込む(x > 0)
        while True:
            x = int(input('整数値：'))
            if x > 0:
                break
            print('整数値は正の整数を入力すること')

        # 進数rを読み込む(r > 0)
        while True:
            r = int(input('進数：'))
            if r > 0:
                break
            print('進数は正の整数を入力すること')

        print(f'整数値"{x}"は{r}進数では"{card_conv(x, r)}"')

        retry = input('もう一度行いますか(Y...はい/N...いいえ)：')
        if retry in {'N', 'n'}:
            break