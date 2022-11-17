def solve(K, R):
    dp = [[0]*(2**K) for _ in range(K)]

    for i in range(K):
        for j in range(2**K):
            if i == 0:
                if j % 2 == 0:
                    dp[i][j] = prob(R, j, j+1)
                else:
                    dp[i][j] = prob(R, j, j-1)

            else:
                if j >> i & 1:
                    c = -1
                else:
                    c = 1

                for k in range(2**i):
                    next_j = (j >> i) + c
                    next_j = (next_j << i) + k
                    dp[i][j] += dp[i-1][j] * dp[i-1][next_j] * prob(R, j, next_j)

    return dp[K-1]

def prob(R, i, j):
    return 1/(1+10**((R[j]-R[i])/400))

def main():
    K = int(input())
    R = [int(input()) for _ in range(2**K)]
    # print(solve(K, R))
    ans = solve(K, R)
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
