def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solve(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    return gcd(abs(x2-x1), abs(y2-y1)) - 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    print(solve(x1, y1, x2, y2))

if __name__ == '__main__':
    main()

""" 入力例
1 11 5 3
"""

""" 出力例
3
"""
