def solve(n, a, m, K):
    dp = [[-1] * (K + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][0] = a[i]

    for i in range(n):
        for j in range(K+1):
            if dp[i][j] >= 0:
                dp[i+1][j] = m[i]
            elif j - a[i] >= 0 and dp[i+1][j-a[i]] > 0:
                dp[i+1][j] = dp[i+1][j-a[i]] - 1
            else:
                dp[i+1][j] = -1

    print(dp)

    return dp[n][K] >= 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = list(map(int, input().split()))
    K = int(input())
    if solve(n, a, m, K):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()


""" 入力例
3
3 5 8
3 2 2
17
"""

""" 出力例
Yes
"""
