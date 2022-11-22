def solve(N, W, v, w):
    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]] + v[i])

    return dp[N][W]

def main():
    N, W = map(int, input().split())
    v = []
    w = []
    for _ in range(N):
        vv, ww = map(int, input().split())
        v.append(vv)
        w.append(ww)

    print(solve(N, W, v, w))

if __name__ == '__main__':
    main()
