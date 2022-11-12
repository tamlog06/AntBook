def solve(N, K, L):
    INF = 1e5
    lb = 1
    ub = INF

    # while ub - lb >= 1e-2:
    for i in range(100):
        if ub - lb < 1e-2:
            break
        mid = (lb + ub) / 2
        if C(mid, L, K):
            lb = mid
        else:
            ub = mid

    import math
    return f'{(math.floor(lb * 100) / 100):.2f}'

def C(x, L, K):
    res = 0
    for l in L:
        res += l // x

    return res >= K


def main():
    N = int(input())
    K = int(input())
    L = list(map(float, input().split()))
    print(solve(N, K, L))

if __name__ == '__main__':
    main()

""" 入力例
4
11
8.02 7.43 4.57 5.39
"""

""" 出力例
2.00
"""
