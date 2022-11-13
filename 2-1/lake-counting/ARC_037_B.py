import sys
sys.setrecursionlimit(1000000)

def solve():
    global N, M, edges, see
    ans = 0
    see = [False] * (N + 1)

    for i in range(1, N+1):
        if not see[i]:
            if dfs(i):
                ans += 1

    return ans

def dfs(x, prev=None):
    global edges, see

    see[x] = True
    for y in edges[x]:
        if y == prev:
            continue

        if see[y]:
            return False
        elif not dfs(y, x):
            return False

    return True

def main():
    global N, M, edges
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    print(solve())

if __name__ == '__main__':
    main()
