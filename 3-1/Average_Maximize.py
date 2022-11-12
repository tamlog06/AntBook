def solve(n, k, wv):
    lb = 0
    ub = 1e6

    for i in range(100):
        mid = (lb + ub) / 2
        res, avg = C(mid, n, k, wv)
        if res:
            lb = mid
        else:
            ub = mid

    return avg

def C(x, n, k, wv):
    y = []
    for i in range(n):
        y.append((wv[i][1] - x*wv[i][0], wv[i][2]))

    y.sort(reverse=True, key=lambda x: x[0])

    res = 0
    val = 0
    weight = 0
    for i in range(k):
        res += y[i][0]
        val += wv[y[i][1]][1]
        weight += wv[y[i][1]][0]

    avg = val / weight

    return res >= 0, avg

def main():
    n = int(input())
    k = int(input())
    wv = []
    for i in range(n):
        w_, v_ = map(int, input().split())
        wv.append((w_, v_, i))

    print(solve(n, k, wv))

if __name__ == '__main__':
    main()

""" 入力例
3
2
2 2
5 3
2 1
"""

""" 出力例
0.75
"""
