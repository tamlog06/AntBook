def solve(N, cost):
    mincost = [float('inf')] * N
    used = [False] * N
    mincost[0] = 0
    res = 0

    while True:
        v = -1
        for u in range(N):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u

        if v == -1:
            break

        used[v] = True
        res += mincost[v]

        for u in range(N):
            mincost[u] = min(mincost[u], cost[v][u])

    return res


def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    cost_matrix = [[float('inf')]*N for _ in range(N)]
    for x, y, z in edges:
        cost_matrix[x][y] = z
        cost_matrix[y][x] = z

    print(solve(N, cost_matrix))

if __name__ == '__main__':
    main()

""" 入力例
7 9
0 1 10
0 3 2
2 3 1
3 4 7
1 4 5
3 5 3
4 5 1
4 6 8
5 6 5
"""

""" 出力例
17
"""
