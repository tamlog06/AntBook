def solve(n, m, a, M):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i+1][j] = 1
            elif j - a[i] - 1 >= 0:
                # dp[i+1][j-1] = sum(dp[i][j-k] for k in range(a[i]+1)) なんだから、dp[i+1][j-1] >= dp[i][j-a[i]-1] は常に成り立つはずで、最後の+Mは必要ないはず
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j-a[i]-1]) % M
            else:
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M

    return dp[n][m]


def main():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    print(solve(n, m, a, M))

if __name__ == '__main__':
    main()

""" 入力例
3
3
1 2 3
10000
"""

""" 出力例
6
"""
