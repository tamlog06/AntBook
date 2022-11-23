# だいぶ汚い実装になってしまった。機嫌が良くなる回数を０スタートにしなかったせい。
# ただ、遷移を考える際に、勝利回数が０回だと面倒臭いので、こんな感じになってしまった。
# Kが０の場合がコーナーケースになってしまった。

def solve(N, K, a):
    dp = [[float('inf')] * (N) for _ in range(N)]
    dp[0][0] = 1

    S = [a[0]]
    for i in range(1, N):
        S.append(S[-1] + a[i])

    if S[-1] == K:
        return 1
    elif K == 0:
        return 0

    for i in range(N-1):
        for j in range(N):
            if j-1 >= 0:
                if dp[i][j-1] == float('inf'):
                    k = float('inf')
                else:
                    k = -((-dp[i][j-1] * S[i+1]) // S[i])

                    if (dp[i][j-1] / S[i]) == (k / S[i+1]):
                        k += 1

                if k - dp[i][j-1] > a[i+1]:
                    k = float('inf')

                dp[i+1][j] = min(dp[i][j], k)
            else:
                dp[i+1][j] = 1

    for j in range(N-1, -1, -1):
        if dp[N-1][j] <= K:
            return j+1

def main():
    N, K = map(int, input().split())
    a = [int(input()) for _ in range(N)]

    print(solve(N, K, a))

if __name__ == '__main__':
    main()
