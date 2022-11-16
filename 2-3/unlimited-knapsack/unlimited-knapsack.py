def solve(n, w, v, W):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(W):
            if j + 1 - w[i] >= 0:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j+1-w[i]] + v[i])
            else:
                dp[i+1][j+1] = dp[i][j+1]

    return dp[n][W]

def main():
    n = int(input())
    wv = [list(map(int, input().split())) for _ in range(n)]
    w = [wv[i][0] for i in range(n)]
    v = [wv[i][1] for i in range(n)]
    W = int(input())
    print(solve(n, w, v, W))

if __name__ == '__main__':
    main()

""" 入力例
3
3 4
4 5
2 3
7
"""

""" 出力例
10
"""
