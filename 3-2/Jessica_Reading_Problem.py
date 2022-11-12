def solve(P, a):
    N = len(set(a))

    res = P
    s = 0
    t = 0
    d = {}
    num = 0

    while s < P:
        while t < P and num < N:
            if a[t] in d:
                if d[a[t]] == 0:
                    num += 1
                d[a[t]] += 1
            else:
                d[a[t]] = 1

            t += 1

        if num < N:
            break

        res = min(res, t-s)

        if d[a[s]] == 1:
            num -= 1

        d[a[s]] -= 1
        s += 1

    return res

def main():
    P = int(input())
    a = list(map(int, input().split()))

    print(solve(P, a))

if __name__ == '__main__':
    main()

""" 入力例
5
1 8 8 8 1
"""

""" 出力例
2
"""
