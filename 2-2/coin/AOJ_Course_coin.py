def solve(n, m, c):
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(m+1):
        dp[i][0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if j - c[i-1] >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-c[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][n]

def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    print(solve(n, m, c))

if __name__ == '__main__':
    main()
