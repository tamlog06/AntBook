import sys
sys.setrecursionlimit(1000000)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def solve():
    global w, h, maze
    ans = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 1:
                ans += 1
                dfs(i, j)

    return ans

def dfs(i, j):
    global w, h, maze

    maze[i][j] = 0
    for sx, sy in zip(dx, dy):
        nx = i + sx
        ny = j + sy
        if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 1:
            dfs(nx, ny)

def main():
    global w, h, maze
    ans = []
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        maze = [list(map(int, input().split())) for _ in range(h)]
        ans.append(solve())

    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
