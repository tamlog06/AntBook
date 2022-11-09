def extgcd(a, b):
    if b == 0:
        return 1, 0, a
    x_prev, y_prev, d = extgcd(b, a%b)
    x = y_prev
    y = x_prev - (a//b)*y_prev

    return x, y, d

def solve(a, b):
    x, y, d = extgcd(a, b)

    if d != 1:
        return -1

    L = [0]*4
    if x > 0:
        L[0] = x
    else:
        L[2] = -x

    if y > 0:
        L[1] = y
    else:
        L[3] = -y

    print(*L)

def main():
    a, b = map(int, input().split())
    solve(a, b)

if __name__ == '__main__':
    main()

""" 入力例
4 11
"""

""" 出力例
3 0 0 1
"""
