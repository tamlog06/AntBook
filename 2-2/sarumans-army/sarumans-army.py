def solve(N, R, X):
    X.sort()

    ans = 0
    i = 0
    while i < N:
        now = X[i]
        while i < N and X[i] - now <= R:
            i += 1
        ans += 1
        now = X[i-1]
        while i < N and X[i] - now <= R:
            i += 1

    return ans

def main():
    N = int(input())
    R = int(input())
    X = list(map(int, input().split()))
    print(solve(N, R, X))

if __name__ == '__main__':
    main()


""" 入力例
6
10
1 7 15 20 30 50
"""

""" 出力例
3
"""
