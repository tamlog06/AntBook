def solve(N, l, r):
    dp = [float('inf')] * N
    import bisect

    l, r = zip(*sorted(zip(l, r), key=lambda x: (x[1], x[0]), reverse=True))
    ans = 0

    for i in range(N):
        index = bisect.bisect_left(dp, l[i])
        dp[index] = l[i]
        ans = max(ans, index + 1)

    return ans

def main():
    N = int(input())
    l = []
    r = []
    for _ in range(N):
        x, r_ = map(int, input().split())
        l.append(x - r_)
        r.append(x + r_)

    print(solve(N, l, r))

if __name__ == '__main__':
    main()
