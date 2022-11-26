def solve(N, h, w):
    # dp = [[float('inf'), float('inf')]] * N
    dp = [float('inf')] * N

    h, w = zip(*sorted(zip(h, w), key=lambda x: (x[0], -x[1])))

    import bisect
    ans = 0
    for i in range(N):
        index = bisect.bisect_left(dp, w[i])
        dp[index] = w[i]
        ans = max(ans, index+1)

    return ans

def main():
    N = int(input())
    w, h = [], []
    for _ in range(N):
        w_, h_ = map(int, input().split())
        w.append(w_)
        h.append(h_)

    print(solve(N, h, w))

if __name__ == '__main__':
    main()
