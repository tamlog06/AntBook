def solve(s1, s2):
    N = len(s1)
    M = len(s2)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        dp[i+1][0] = i + 1

    for j in range(M):
        dp[0][j+1] = j + 1

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
            else:
                dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)

    return dp[N][M]


def main():
    s1 = input()
    s2 = input()
    print(solve(s1, s2))

if __name__ == '__main__':
    main()
