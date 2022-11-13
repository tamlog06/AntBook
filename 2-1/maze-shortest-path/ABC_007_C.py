dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    global R, C, sx, sy, gx, gy, maze
    que = [(sx, sy)]
    while que:
        qx, qy = que.pop(0)
        if qx == gx and qy == gy:
            break
        for xx, yy in zip(dx, dy):
            nx, ny = qx+xx, qy+yy
            if 0 <= nx < C and 0 <= ny < R and maze[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[qy][qx] + 1
                que.append((nx, ny))

    return dist[gy][gx]


def main():
    global R, C, sx, sy, gx, gy, maze, dist
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy, sx = sy-1, sx-1
    gy, gx = gy-1, gx-1
    maze = [list(input()) for _ in range(R)]
    dist = [[-1]*C for _ in range(R)]
    dist[sy][sx] = 0
    print(solve())

if __name__ == '__main__':
    main()
