dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 's':
                sx, sy = i, j
                dist[i][j] = 0
            elif maze[i][j] == 'g':
                gx, gy = i, j

    from collections import deque
    que = deque()
    que.append((sx, sy))
    while que:
        qx, qy = que.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = qx+xx, qy+yy
            if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == float('inf'):
                if maze[nx][ny] == 'g':
                    dist[nx][ny] = dist[qx][qy]
                    break
                elif maze[nx][ny] == '#' and dist[qx][qy] <= 1:
                    dist[nx][ny] = dist[qx][qy] + 1
                    que.append((nx, ny))
                elif maze[nx][ny] == '.':
                    dist[nx][ny] = dist[qx][qy]
                    que.appendleft((nx, ny))

    if dist[gx][gy] <= 2:
        return 'YES'
    else:
        return 'NO'


def main():
    global H, W, maze, dist
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    dist = [[float('inf')]*W for _ in range(H)]
    print(solve())

if __name__ == '__main__':
    main()
