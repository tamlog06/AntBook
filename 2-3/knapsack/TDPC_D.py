def solve(N, D):
    A, B, C = 0, 0, 0
    while D % 2 == 0:
        A += 1
        D //= 2

    while D % 3 == 0:
        B += 1
        D //= 3

    while D % 5 == 0:
        C += 1
        D //= 5


    if D != 1:
        return 0


    dp = [[[[0]*(C+1) for _ in range(B+1)] for __ in range(A+1)] for ___ in range(N+1)]

    dp[0][0][0][0] = 1

    for n in range(N):
        for a in range(A+1):
            for b in range(B+1):
                for c in range(C+1):
                    dp[n+1][a][b][c] += dp[n][a][b][c] * 1/6
                    dp[n+1][min(A, a+1)][b][c] += dp[n][a][b][c] * 1/6
                    dp[n+1][a][min(B, b+1)][c] += dp[n][a][b][c] * 1/6
                    dp[n+1][min(A, a+2)][b][c] += dp[n][a][b][c] * 1/6
                    dp[n+1][a][b][min(C, c+1)] += dp[n][a][b][c] * 1/6
                    dp[n+1][min(A, a+1)][min(B, b+1)][c] += dp[n][a][b][c] * 1/6

    return dp[N][A][B][C]

def main():
    N, D = map(int, input().split())
    print(solve(N, D))

if __name__ == '__main__':
    main()
