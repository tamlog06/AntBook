import bisect

def solve(N, a):
    dp = [float('inf')] * N
    ans = 0
    for i in range(N):
        index = bisect.bisect_left(dp, a[i])
        dp[index] = a[i]
        ans = max(ans, index+1)

    return ans

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(solve(N, a))

if __name__ == '__main__':
    main()
