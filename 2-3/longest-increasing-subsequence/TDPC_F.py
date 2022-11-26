# 無理。また戻ってとく
MOD = 1e9+7

def solve(N, K):
    dp = [0] * (N+2)
    dp[0] = 1
    acc = [0] * (N+3)
    acc[1] = 1

    for i in range(1, N+2):
        if i != 1 and i != N:
            dp[i] = (acc[i] - acc[max(0, i-K-1)]+MOD) % MOD
        acc[i+1] = (acc[i] + dp[i]) % MOD 
    
    print(dp)

    return dp[N+1]

def main():
    N, K = map(int, input().split())
    print(solve(N, K))

if __name__ == '__main__':
    main()
