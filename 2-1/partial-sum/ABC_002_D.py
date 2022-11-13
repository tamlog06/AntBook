def solve(N, M, mat):
    ans = 1
    for i in range(2**N):
        res = []
        for j in range(N):
            if ((i >> j) & 1):
                res.append(j)

        if check(mat, res):
            ans = max(ans, len(res))

    return ans

def check(mat, res):
    for i in res:
        for j in res:
            if i == j:
                continue
            if mat[i][j] == -1:
                return False

    return True

def main():
    N, M = map(int, input().split())
    matrix = [[-1 for _ in range(N)] for __ in range(N) ]
    for _ in range(M):
        x, y = map(int, input().split())
        matrix[x-1][y-1] = 1
        matrix[y-1][x-1] = 1

    print(solve(N, M, matrix))

if __name__ == '__main__':
    main()
