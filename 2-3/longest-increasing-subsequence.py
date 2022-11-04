def solve(n, a):
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n):
        for j in range(n):
            if a[i] > dp[j]:
                dp[j+1] = min(dp[j+1], a[i])

    for i in range(n, -1, -1):
        if dp[i] < float('inf'):
            return i

def solve2(n, a):
    import bisect
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n):
        j = bisect.bisect_left(dp, a[i])
        dp[j] = a[i]

    for i in range(n, -1, -1):
        if dp[i] < float('inf'):
            return i

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
    print(solve2(n, a))

if __name__ == '__main__':
    main()


""" 入力例
5
4 2 3 1 5
"""

""" 出力例
3
"""
