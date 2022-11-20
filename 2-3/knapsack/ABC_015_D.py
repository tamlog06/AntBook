# PythonだとTLE, 3重リストでdpを作るとMLE. PyPyで通すには、２重リストでdpを作る必要がある。この場合でもPythonだとTLE
def solve(W, N, K, A, B):
    # dp = [[[0] * (W+1) for _ in range(K+1)] for _ in range(N+1)]

    # for i in range(1, N+1):
        # for j in range(1, K+1):
            # for k in range(W+1):
                # if k > 0:
                    # dp[i][j][k] = dp[i][j][k-1]

                # if k - A[i-1] >= 0:
                    # dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k], dp[i-1][j-1][k-A[i-1]] + B[i-1])
                # else:
                    # dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
    # return max(dp[N][K])

    dp = [[0] * (W+1) for _ in range(K+1)]

    for i in range(N):
        for j in range(K, 0, -1):
            for k in range(W, -1, -1):

                if k - A[i] >= 0:
                    dp[j][k] = max(dp[j][k], dp[j-1][k-A[i]] + B[i])
    
    return max(dp[K])


def main():
    W = int(input())
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = []
    B = []
    for a, b in AB:
        A.append(a)
        B.append(b)

    print(solve(W, N, K, A, B))


if __name__ == '__main__':
    main()
