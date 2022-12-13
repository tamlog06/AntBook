import heapq
def solve(N, R, cost_matrix):
    d = [[float('inf')]*2 for _ in range(N)]
    d[0][0] = 0

    que = [(0, 0)]
    while que:
        distance, node = heapq.heappop(que)
        if d[node][0] < distance and d[node][1] < distance:
            continue

        for i in range(N):
            if d[i][0] < distance + cost_matrix[node][i]:
                if d[i][1] < distance + cost_matrix[node][i]:
                    continue
                else:
                    d[i][1] = distance + cost_matrix[node][i]
                    heapq.heappush(que, (d[i][1], i))
            else:
                d[i][1] = d[i][0]
                d[i][0] = distance + cost_matrix[node][i]
                heapq.heappush(que, (d[i][0], i))
                heapq.heappush(que, (d[i][1], i))

    return d[N-1][1]

def main():
    N, R = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(R)]
    cost_matrix = [[float('inf')]*N for _ in range(N)]
    for x, y, z in edges:
        cost_matrix[x][y] = z
        cost_matrix[y][x] = z
    print(solve(N, R, cost_matrix))

if __name__ == '__main__':
    main()

""" 入力例
4 4
0 1 100
1 2 250
1 3 200
2 3 100
"""

""" 出力例
450
"""
