def solve(N, p):
    M = sum(p)
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(M+1):
            if dp[i][j]:
                dp[i+1][j] = True
                dp[i+1][j+p[i]] = True

    return sum(dp[N])

def main():
    N = int(input())
    p = list(map(int, input().split()))
    print(solve(N, p))

if __name__ == '__main__':
    main()
