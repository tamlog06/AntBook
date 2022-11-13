dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    global H, W, N, maze, dist, position
    sign = [('S', '1')]
    for i in range(1, N):
        sign.append((str(i), str(i+1)))

    ans = 0
    for i in range(N):
        sx, sy = position[sign[i][0]]
        dist[i][sx][sy] = 0
        ans += bfs(sign[i][0], sign[i][1], i)
    return ans

def bfs(fro, to, index):
    global H, W, N, maze, dist, position
    sx, sy = position[fro]
    gx, gy = position[to]

    que = [(sx, sy)]
    while que:
        qx, qy = que.pop(0)
        if qx == gx and qy == gy:
            break

        for xx, yy in zip(dx, dy):
            nx = qx + xx
            ny = qy + yy
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != 'X' and dist[index][nx][ny] == -1:
                dist[index][nx][ny] = dist[index][qx][qy] + 1
                que.append((nx, ny))

    return dist[index][gx][gy]

def main():
    global H, W, N, maze, dist, position
    H, W, N = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    dist = [[[-1 for _ in range(W)] for __ in range(H)] for ___ in range(N)]

    position = {}
    for i in range(H):
        for j in range(W):
            if maze[i][j] != '.' and maze[i][j] != 'X':
                position[maze[i][j]] = (i, j)

    print(solve())

if __name__ == '__main__':
    main()
