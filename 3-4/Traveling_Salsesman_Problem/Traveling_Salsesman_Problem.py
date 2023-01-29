# Solution 1

N, M  = map(int, input().split())
edges = [[float('inf') for _ in range(N)] for _ in range(N)]

for _ in range(M):
    v, u, w = map(int, input().split())
    edges[v][u] = w

dp = [[-1 for _ in range(N)] for _ in range(1 << N)]

def rec(S, v):
    if dp[S][v] >= 0:
        return dp[S][v]

    if S == (1 << N) -1 and v == 0:
        dp[S][v] = 0
        return 0

    res = float('inf')
    for u in range(N):
        if not S >> u & 1:
            res = min(res, rec(S | 1 << u, u) + edges[v][u])

    dp[S][v] = res
    return res

print(rec(0, 0))

# Solution 2

def solve():
    dp = [[float('inf') for _ in range(N)] for _ in range(1 << N)]
    dp[(1<<N)-1][0] = 0

    for S in range((1<<N)-2, -1, -1):
        for v in range(N):
            for u in range(N):
                if not S >> u & 1:
                    dp[S][v] = min(dp[S][v], dp[S | 1 << u][u] + edges[v][u])

    return dp[0][0]

print(solve())

"""
入力例1
--------------
5 8
0 1 3
0 3 4
1 2 5
2 0 4
2 3 5
3 4 3
4 1 6
4 0 7
"""
