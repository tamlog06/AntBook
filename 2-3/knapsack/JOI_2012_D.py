def solve(D, N, T, A, B, C):
    dp = [[-float('inf')]*N for _ in range(D+1)]

    for j in range(N):
        dp[0][j] = 0

    for i in range(1, D+1):
        for j in range(N):
            if A[j] <= T[i-1] <= B[j]:
                if i == 1:
                    dp[i][j] = 0
                else:
                    for k in range(N):
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(C[j] - C[k]))

    return max(dp[D])

def main():
    D, N = map(int, input().split())
    T = [int(input()) for _ in range(D)]
    A, B, C = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    print(solve(D, N, T, A, B, C))

if __name__ == '__main__':
    main()
