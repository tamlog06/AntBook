def solve(n, w, v, W):
    V = sum(v)
    dp = [[float('inf')] * (V+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0

    for i in range(n):
        for j in range(V+1):
            if j - w[i] >= 0:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])
            else:
                dp[i+1][j] = dp[i][j]

    for i in range(V, -1, -1):
        if dp[n][i] <= W:
            return i

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
4
2 3
1 2
3 4
2 2
5
"""

""" 出力例
7
"""
