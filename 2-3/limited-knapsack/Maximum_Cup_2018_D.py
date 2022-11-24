def solve(N, M, L, X, a):
    dp = [[float('inf')] * M for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(M):
            c = -(-M+j-a[i]+1) // M
            # print(-M+j-a[i], c)
            dp[i+1][j] = min(dp[i][j], dp[i][(j-a[i])%M] + c)

    if dp[N][L] <= X:
        return 'Yes'
    else:
        return 'No'

def main():
    N, M, L, X = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(N, M, L, X, a))

if __name__ == '__main__':
    main()
