def solve(H, N, A, B):
    dp = [[float('inf')] * (H+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(H+1):
            # if j - A[i] >= 0:
                # dp[i+1][j] = min(dp[i][j], dp[i+1][j-A[i]] + B[i])
            # else:
                # dp[i+1][j] = dp[i][j]
            dp[i+1][j] = min(dp[i][j], dp[i+1][max(0, j-A[i])] + B[i])

    return dp[N][H]

def main():
    H, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(solve(H, N, A, B))

if __name__ == '__main__':
    main()
