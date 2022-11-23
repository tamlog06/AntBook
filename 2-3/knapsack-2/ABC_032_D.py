# 想定通り、パターン１がTLEで通らない。半分全列挙というのをするようで、中級編でやる内容のようなので、後で戻ってきて解く。

def solve1(W):
    return dfs(0, W, 0)

def dfs(i, W, value):
    if i == N:
        return value

    if W - w[i] >= 0:
        return max(dfs(i+1, W, value), dfs(i+1, W-w[i], value+v[i]))
    else:
        return dfs(i+1, W, value)

def solve2(W, Sw):
    if Sw <= W:
        return sum(v)

    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j-w[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]

    return max(dp[N])

def solve3(W, Sv):
    dp = [[float('inf')] * (Sv+1) for _ in range(N+1)]
    dp[0][0] = 0
    ans = 0

    for i in range(N):
        for j in range(Sv+1):
            if j-v[i] >= 0:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])
            else:
                dp[i+1][j] = dp[i][j]

            if i == N-1 and dp[N][j] <= W:
                ans = j

    return ans

def main():
    global N, v, w
    N, W = map(int, input().split())
    v = []
    w = []
    sv = 0
    sw = 0
    v_max = 0
    w_max = 0
    for _ in range(N):
        vv, ww = map(int, input().split())
        v.append(vv)
        w.append(ww)

        sv += vv
        sw += ww

        v_max = max(v_max, vv)
        w_max = max(w_max, ww)

    if N <= 30:
        print(solve1(W))
    elif w_max <= 1000:
        print(solve2(W, sw))
    else:
        print(solve3(W, sv))


if __name__ == '__main__':
    main()
    
