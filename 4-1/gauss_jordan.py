
def gauss_jordan(A, b):
    N = len(A)
    B = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = A[i][j]

    # 行列Aの後ろにbを並べて拡大係数行列を作る
    for i in range(N):
        B[i].append(b[i])

    for i in range(N):
        # 注目している変数の係数の絶対値が大きい式をi番目に持ってくる
        pivot = i
        for j in range(i, N):
            if abs(B[j][i]) > abs(B[pivot][i]):
                pivot = j
        B[i], B[pivot] = B[pivot], B[i]

        #行列が正則でない
        if abs(B[i][i]) < 1e-10:
            return False

        for j in range(i+1, N+1):
            B[i][j] /= B[i][i]

        for j in range(N):
            if i != j:
                for k in range(i+1, N+1):
                    B[j][k] -= B[j][i] * B[i][k]

    x = [0] * N
    for i in range(N):
        x[i] = B[i][N]

    return x
