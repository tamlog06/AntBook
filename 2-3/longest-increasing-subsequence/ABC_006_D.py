def solve(N, c):
    dp = [float('inf')] * N

    import bisect
    ans = 0
    for i in range(N):
        index = bisect.bisect_left(dp, c[i])
        dp[index] = c[i]
        ans = max(ans, index+1)

    return N - ans


def main():
    N = int(input())
    c = list(int(input()) for _ in range(N))
    print(solve(N, c))

if __name__ == '__main__':
    main()
