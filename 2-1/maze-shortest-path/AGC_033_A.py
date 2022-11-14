dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

from collections import deque
# listのpop(0)はO(N)だが、dequeを使うとO(1)になるらしい。これじゃないと通らない。
def solve():
    # que = []
    que = deque()
    for i in range(H):
        for j in range(W):
            if maze[i][j] == '#':
                dist[i][j] = 0
                que.append((i, j))

    ans = 0
    while que:
        # qx, qy = que.pop(0)
        qx, qy = que.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = qx+xx, qy+yy
            if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == float('inf'):
                dist[nx][ny] = dist[qx][qy] + 1
                ans = max(ans, dist[nx][ny])
                que.append((nx, ny))

    return ans

def main():
    global H, W, N, maze, dist
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    dist = [[float('inf')]*W for _ in range(H)]
    print(solve())

if __name__ == '__main__':
    main()
