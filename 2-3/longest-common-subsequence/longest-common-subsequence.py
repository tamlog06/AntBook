def solve(n, m, s, t):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i][j] + 1, dp[i][j+1], dp[i+1][j])
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[n][m]

def main():
    n = int(input())
    m = int(input())
    s = input()
    t = input()
    print(solve(n, m, s, t))

if __name__ == '__main__':
    main()


""" 入力例
4
4
abcd
becd
"""

""" 出力例
3
"""
