import bisect

def solve1(n, S, a):
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])

    if s[-1] < S:
        return 0

    res = n
    for i in range(1, n+1):
        lb = i
        ub = n

        if s[ub] - s[lb-1] < S:
            break

        t = bisect.bisect_left(s, S+s[lb-1])

        res = min(res, t-lb+1)

    return res

def solve2(n, S, a):
    s = 0
    t = 0
    sum = 0
    res = n+1

    while s < n:
        while t < n and sum < S:
            sum += a[t]
            t += 1

        if sum < S:
            break

        res = min(res, t-s)
        sum -= a[s]
        s += 1

    if res > n:
        return 0

    return res

def main():
    n = int(input())
    S = int(input())
    a = list(map(int, input().split()))

    print(solve1(n, S, a))
    print(solve2(n, S, a))


if __name__ == '__main__':
    main()

""" 入力例
10
15
5 1 3 5 10 7 4 9 2 8
"""

""" 出力例
2
"""

""" 入力例
5
11
1 2 3 4 5
"""

""" 出力例
3
"""
