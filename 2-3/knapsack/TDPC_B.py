def solve(A, B, a, b):
    dp = [[0]*(B+1) for _ in range(A+1)]
    dp[0][0] = 0
    for i in range(1, A+1):
        dp[i][0] = a[-i] - dp[i-1][0]

    for i in range(1, B+1):
        dp[0][i] = b[-i] - dp[0][i-1]

    for i in range(1, A+1):
        for j in range(1, B+1):
            dp[i][j] = max(a[-i] - dp[i-1][j], b[-j] - dp[i][j-1])

    ans = (sum(a) + sum(b) + dp[A][B]) // 2
    return ans


def main():
    A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(A, B, a, b))

if __name__ == '__main__':
    main()
