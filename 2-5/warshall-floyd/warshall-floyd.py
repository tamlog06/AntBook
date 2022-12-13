def solve(n, cost, s, g):
    dp = [[float('inf')] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            elif cost[i][j] == -1:
                dp[i][j] = float('inf')
            else:
                dp[i][j] = cost[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(n):
        print(*dp[i])
    return dp[s][g]

def main():
    n, e = map(int, input().split())
    s, g = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    cost_matrix = [[-1]*n for _ in range(n)]
    for x, y, z in edges:
        cost_matrix[x][y] = z
        cost_matrix[y][x] = z

    print(solve(n, cost_matrix, s, g))

if __name__ == '__main__':
    main()

""" 入力例
7 10
0 6
0 1 2
0 2 5
1 2 4
1 3 6
2 3 2
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9
"""

""" 出力例
16
"""


