def solve(maze, N, M):
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 'S':
                S = (i, j)
            elif maze[i][j] == 'G':
                G = (i, j)

    return bfs(maze, S, G, N, M)
    

def bfs(maze, S, G, N, M):
    d = [[-1] * M for _ in range(N)]
    d[S[0]][S[1]] = 0
    que = [S]

    while que:
        p = que.pop(0)
        if maze[p[0]][p[1]] == 'G':
            break

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for xx, yy in zip(dx, dy):
            nx = p[0] + xx
            ny = p[1] + yy
            if 0 <= nx < N and 0 <= ny < M and d[nx][ny] == -1 and maze[nx][ny] != '#':
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1


    return d[G[0]][G[1]]

def main():
    N, M = map(int, input().split())
    maze = [list(input()) for _ in range(N)]
    print(solve(maze, N, M))

if __name__ == '__main__':
    main()


""" 入力例
10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
"""

""" 出力例
22
"""

