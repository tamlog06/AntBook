MOD = 1e9 + 7

def solve(D, N):
    pow_N = len(str(N))
    S = str(N)
    dp = [[[0] * D for _ in range(2)] for __ in range(pow_N+1)]

    dp[0][0][0] = 1

    for i in range(pow_N):
        for j in range(D):
            for smaller in range(2):
                for k in range(10):
                    if smaller == 0 and k > int(S[i]):
                        break

                    if smaller == 1 or k < int(S[i]):
                        next_smaller = 1
                    else:
                        next_smaller = 0

                    dp[i+1][next_smaller][(j+k) % D] += dp[i][smaller][j]
                    dp[i+1][next_smaller][(j+k) % D] %= MOD

    return int((dp[pow_N][0][0] + dp[pow_N][1][0] - 1) % MOD)


def main():
    D = int(input())
    N = int(input())
    print(solve(D, N))

if __name__ == '__main__':
    main()
