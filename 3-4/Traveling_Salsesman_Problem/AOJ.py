def solve(V, E, s, t, d):
    global edges, dp, N
    N = V
    edges = [[float('inf') for _ in range(V)] for _ in range(V)]

    for i in range(E):
        edges[s[i]][t[i]] = d[i]

    dp = [[-1 for _ in range(V)] for _ in range(1 << V)]

    return rec(0, 0, dp)


def rec(S, v, dp):
    global egdes, N

    if dp[S][v] >= 0:
        return dp[S][v]

    if S == (1 << N) - 1 and v == 0:
        dp[S][v] = 0
        return 0

    res = float('inf')
    for u in range(N):
        if not S >> u & 1:
            res = min(res, rec(S | 1 << u, u, dp) + edges[v][u])

    dp[S][v] = res
    return res


def main():
    V, E = map(int, input().split())
    s, t, d = [], [], []
    for _ in range(E):
        ss, tt, dd = map(int, input().split())
        s.append(ss)
        t.append(tt)
        d.append(dd)

    ans = solve(V, E, s, t, d)
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
