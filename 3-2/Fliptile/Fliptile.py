def solve(N, M, tile):
    min_res = float('inf')
    matrix = []
    for i in range(2**N):
        flip = [[0]*N for _ in range(M)]
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                flip[0][N-1-j] = 1
                count += 1

        res, mat = calc(tile, flip, N, M)
        if min_res > res + count:
            min_res = res + count
            matrix = mat

    if min_res == float('inf'):
        return False, 'IMPOSSIBLE'
    else:
        return True, matrix

def calc(tile, flip, N, M):
    res = 0
    # for i in range(1, M-1):
    for i in range(1, M):
        for j in range(N):
            if check(tile, flip, i-1, j, N, M) == 1:
                flip[i][j] = 1
                res += 1

    # for j in range(N):
        # if check(tile, flip, M-2, j, N, M) == 1:
            # if check(tile, flip, M-1, j, N, M) == 1:
                # flip[M-1][j] = 1
                # res += 1
            # else:
                # return float('inf'), None
        # else:
            # if check(tile, flip, M-1, j, N, M) == 1:
                # return float('inf'), None
            # else:
                # continue

    for j in range(N):
        if check(tile, flip, M-1, j, N, M) == 1:
            return float('inf'), None

    return res, flip

def check(tile, flip, i, j, N, M):
    sx = [0, 1, 0, -1, 0]
    sy = [0, 0, 1, 0, -1]
    res = tile[i][j]

    for dx, dy in zip(sx, sy):
        nx = i + dx
        ny = j + dy
        if 0 <= nx < M and 0 <= ny < N:
            res += flip[nx][ny]

    return res % 2

def main():
    M, N = map(int, input().split())
    tile = [list(map(int, input().split())) for _ in range(M)]
    # print(solve(N, M, tile))

    ret, val = solve(N, M, tile)
    print()
    if ret:
        for i in range(M):
            print(*val[i])
    else:
        print(val)



if __name__ == '__main__':
    main()

""" 入力例
4 4
1 0 0 1
0 1 1 0
0 1 1 0
1 0 0 1
"""

""" 出力例
0 0 0 0
1 0 0 1
1 0 0 1
0 0 0 0
"""
