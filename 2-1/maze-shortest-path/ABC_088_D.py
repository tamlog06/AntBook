dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    global H, W, N, maze, dist
    que = [(0, 0)]
    while que:
        qx, qy = que.pop(0)
        if qx == W-1 and qy == H-1:
            break
        for xx, yy in zip(dx, dy):
            nx, ny = qx+xx, qy+yy
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == '.' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[qx][qy] + 1
                que.append((nx, ny))

    if dist[H-1][W-1] == -1:
        return -1

    return H*W - (dist[H-1][W-1]+1) - N

def main():
    global H, W, N, maze, dist
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]
    dist[0][0] = 0

    N = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] == '#':
                N += 1

    print(solve())

if __name__ == '__main__':
    main()
