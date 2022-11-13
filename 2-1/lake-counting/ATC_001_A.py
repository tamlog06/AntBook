import sys
sys.setrecursionlimit(1000000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 's':
                s = (i, j)

    if dfs(s[0], s[1]):
        return 'Yes'
    else:
        return 'No'

def dfs(x, y):
    if 0 <= x < H and 0 <= y < W and maze[x][y] != '#':
        if maze[x][y] == 'g':
            return True
        maze[x][y] = '#'
    else:
        return False

    if dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1):
        return True

    # for sx, sy in zip(dx, dy):
        # nx = x + sx
        # ny = y + sy
        # if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != '#':
            # if maze[nx][ny] == 'g':
                # return True
            # else:
                # if dfs(nx, ny):
                    # return True

    return False

def main():
    global H, W, maze
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    print(solve())

if __name__ == '__main__':
    main()
