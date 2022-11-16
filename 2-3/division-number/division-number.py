# 意味わからんかったけど、これを見て解決
# https://qiita.com/MyOden/items/4cf63128469f5833e4aa

def solve(n, m, M):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m+1):
        for j in range(n+1):
            if j >= i:
                dp[i][j] = (dp[i][j-i] + dp[i-1][j]) % M
            else:
                dp[i][j] = dp[i-1][j] % M

    print(dp)
    return dp[m][n] % M

def main():
    n = int(input())
    m = int(input())
    M = int(input())
    print(solve(n, m, M))

if __name__ == '__main__':
    main()

""" 入力例
4
3
10000
"""

""" 出力例
4
"""
