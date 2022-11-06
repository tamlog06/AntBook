def solve(n, cost, s, g):
    d = [float('inf')] * n
    d[s] = 0
    used = [False] * n

    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        elif v == g:
            break

        used[v] = True

        for u in range(n):
            if cost[v][u] != -1:
                d[u] = min(d[u], d[v] + cost[v][u])

    return d[g]

import heapq
def solve_heap(n, cost, s, g):
    d = [float('inf')] * n
    d[s] = 0
    que = [(0, s)]
    while que:
        distance, node = heapq.heappop(que)
        if d[node] < distance:
            continue
        if node == g:
            break

        for to, to_cost in cost[node].items():
            if d[to] > d[node] + to_cost:
                d[to] = d[node] + to_cost
                heapq.heappush(que, (d[to], to))

    return d[g]

def main():
    n, e = map(int, input().split())
    s, g = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    cost_matrix = [[-1]*n for _ in range(n)]
    for x, y, z in edges:
        cost_matrix[x][y] = z
        cost_matrix[y][x] = z

    cost_list = [{} for _ in range(n)]
    for x, y, z in edges:
        cost_list[x][y] = z
        cost_list[y][x] = z

    print(solve(n, cost_matrix, s, g))
    print(solve_heap(n, cost_list, s, g))

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


