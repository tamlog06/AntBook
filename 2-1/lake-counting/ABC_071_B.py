from copy import deepcopy
import sys
sys.setrecursionlimit(1000000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    global maze_init, count, N
    N = 0

    for i in range(H):
        for j in range(W):
            if maze[i][j] == 'o':
                N += 1

    for i in range(H):
        for j in range(W):
            maze_init = deepcopy(maze)
            maze_init[i][j] = 'o'
            count = -1
            if dfs(i, j):
                return 'YES'

    return 'NO'

def dfs(i, j):
    global count, N
    maze_init[i][j] = 'x'
    count += 1

    for sx, sy in zip(dx, dy):
        nx = i + sx
        ny = j + sy
        if 0 <= nx < H and 0 <= ny < W and maze_init[nx][ny] == 'o':
            dfs(nx, ny)

    if count == N:
        return True

    return False


def main():
    global H, W, maze
    H, W = 10, 10
    maze = [list(input()) for _ in range(H)]
    print(solve())

if __name__ == '__main__':
    main()
