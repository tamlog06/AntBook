def solve(A, B, a, b):
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    a = [0] + a[::-1]
    b = [0] + b[::-1]

    for i in range(A):
        dp[i+1][0] = a[i+1] - dp[i][0]

    for j in range(B):
        dp[0][j+1] = b[j+1] - dp[0][j]

    for i in range(1, A+1):
        for j in range(1, B+1):
            dp[i][j] = max(a[i] - dp[i-1][j], b[j] - dp[i][j-1])

    ans = (sum(a) + sum(b) + dp[A][B])//2
    return ans

def main():
    A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(A, B, a, b))

if __name__ == '__main__':
    main()
