def solve(field, N, M):
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W':
                dfs(field, i, j, N, M)
                count += 1

    return count

def dfs(field, x, y, N, M):
    field[x][y] = '.'
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for xx, yy in zip(dx, dy):
        nx = x + xx
        ny = y + yy
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'W':
            dfs(field, nx, ny, N, M)

def main():
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    print(solve(field, N, M))

if __name__ == '__main__':
    main()

""" 入力例
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
"""

""" 出力例
3
"""
