def solve(n, s, l, p, m, w):
    dp = [-1] * 394
    dp[0] = 0

    for i in range(n):
        for j in range(394):
            for k in range(s[i], l[i]+1):
                if j-k >= 0 and dp[j-k] >= 0:
                    dp[j] = max(dp[j], dp[j-k] + p[i])
                    break

    ans = []
    for i in range(m):
        if dp[w[i]] == -1:
            return [-1]
        ans.append(dp[w[i]])

    return ans

def main():
    n = int(input())
    s, l, p = [], [], []
    for _ in range(n):
        s_, l_, p_ = map(int, input().split())
        s.append(s_)
        l.append(l_)
        p.append(p_)

    m = int(input())
    w = [int(input()) for _ in range(m)]

    ans = solve(n, s, l, p, m, w)
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
