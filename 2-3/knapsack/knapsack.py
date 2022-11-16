def solve(N, w, v, W):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j - w[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return max(dp[N])

def main():
    N = int(input())
    wv = [list(map(int, input().split())) for _ in range(N)]
    w = [wv[i][0] for i in range(N)]
    v = [wv[i][1] for i in range(N)]
    W = int(input())
    print(solve(N, w, v, W))

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
