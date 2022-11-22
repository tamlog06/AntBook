def solve(N, M, abcw, xyz):
    dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]

    for a, b, c, w in abcw:
        dp[a][b][c] = max(dp[a][b][c], w)

    for i in range(101):
        for j in range(101):
            for k in range(101):
                dp[i][j][k] = max(dp[i][j][k], dp[max(0, i-1)][j][k], dp[i][max(0, j-1)][k], dp[i][j][max(0, k-1)])

    for x, y, z in xyz:
        print(dp[x][y][z])

def main():
    N, M = map(int, input().split())
    abcw = [tuple(map(int, input().split())) for _ in range(N)]
    xyz = [tuple(map(int, input().split())) for _ in range(M)]

    solve(N, M, abcw, xyz)

if __name__ == '__main__':
    main()
