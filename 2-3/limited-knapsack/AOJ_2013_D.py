def solve(N, M, X, H, edges):
    dist = [[float('inf'), -1]] * (N + 1)
    dist[0] = [0, 0]
    dist[1] = [0, X]
    H = [0] + H

    import heapq
    q = [(dist[1], 1)]
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        if v == N:
            break

        for u, t in edges[v]:
            if H[v] - t >= 0:
                if dist[v][1] - t >= H[u]:
                    T = dist[v][1] - H[u]
                    d_u = dist[v][0] + T
                    h_u = dist[v][1] - T
                elif dist[v][1] - t >= 0:
                    T = t
                    d_u = dist[v][0] + T
                    h_u = dist[v][1] - T
                else:
                    T = t - (dist[v][1] - t)
                    d_u = dist[v][0] + T
                    h_u = 0

                if dist[u][0] > d_u:
                    dist[u] = [d_u, h_u]
                    heapq.heappush(q, (dist[u], u))
    
    if dist[N][0] == float('inf'):
        return -1
    else:
        return dist[N][0] + (H[N] - dist[N][1])



def main():
    N, M, X = map(int, input().split())
    H = list(int(input()) for _ in range(N))
    from collections import defaultdict
    edges = defaultdict(list)
    for _ in range(M):
        a, b, t = map(int, input().split())
        edges[a].append((b, t))
        edges[b].append((a, t))

    print(solve(N, M, X, H, edges))

if __name__ == '__main__':
    main()
