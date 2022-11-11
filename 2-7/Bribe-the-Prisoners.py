def solve(P, Q, A):
    A.sort()
    A = [0] + A + [P+1]

    dp = [[float('inf')]*(Q+2) for _ in range(Q+1)]
    for i in range(Q+1):
        dp[i][i+1] = 0

    for w in range(2, Q+2):
        for i in range(Q+2-w):
            j = i+w

            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[j] - A[i] - 2)

    return dp[0][Q+1]

def main():
    P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(P, Q, A))

if __name__ == '__main__':
    main()

""" 入力例
8 1
3
"""

""" 出力例
7
"""

""" 入力例
20 3
3 6 14
"""

""" 出力例
17
"""
