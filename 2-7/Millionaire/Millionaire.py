def solve(M, P, X):
    N = 1<<M
    dp = [[0.0]*(N+1) for _ in range(M+1)]
    dp[0][-1] = 1.0

    for i in range(1, M+1):
        for j in range(N+1):
            t = dp[i][j]
            for k in range(min(j, N-j)+1):
                t = max(t, P*dp[i-1][j+k] + (1-P)*dp[i-1][j-k])
            dp[i][j] = t

    print(dp)
    return dp[M][X//(1000000//N)]

def main():
    M, P, X = input().split()
    M = int(M)
    P = float(P)
    X = int(X)
    print(solve(M, P, X))

if __name__ == '__main__':
    main()


""" 入力例
1 0.5 500000
"""

""" 出力例
0.5
"""

""" 入力例
3 0.75 600000
"""

""" 出力例
0.843750
"""
