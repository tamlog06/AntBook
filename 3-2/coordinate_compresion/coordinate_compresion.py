from collections import deque

W, H, N = map(int, input().split())
X1 = list(map(int, input().split()))
X2 = list(map(int, input().split()))
Y1 = list(map(int, input().split()))
Y2 = list(map(int, input().split()))


def compress(pt1, pt2, w):
    pts = set()

    for i in range(N):
        for d in [-1, 0, 1]:
            npt1 = pt1[i] + d
            npt2 = pt2[i] + d

            if 1 <= npt1 <= w:
                pts.add(npt1)

            if 1 <= npt2 <= w:
                pts.add(npt2)

    pts = sorted(list(pts))

    p1 = [pts.index(pt1[i]) for i in range(N)]
    p2 = [pts.index(pt2[i]) for i in range(N)]

    return p1, p2, len(pts)

x1, x2, w = compress(X1, X2, W)
y1, y2, h = compress(Y1, Y2, H)

field = [['.'] * w for _ in range(h)]
for i in range(N):
    for x in range(x1[i], x2[i]+1):
        for y in range(y1[i], y2[i]+1):
            field[y][x] = '#'

ans = 0

for x in range(h):
    for y in range(w):
        if field[x][y] == '#':
            continue

        ans += 1

        q = deque()
        q.append((x, y))
        while q:
            sx, sy = q.popleft()
            field[sx][sy] = '#'

            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]

            for ddx, ddy in zip(dx, dy):
                nx = sx + ddx
                ny = sy + ddy

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue

                if field[nx][ny] == '#':
                    continue

                q.append((nx, ny))

print(ans)


"""
10 10 5
1 1 4 9 10
6 10 4 9 10
4 8 1 1 6
4 8 10 5 10
"""
