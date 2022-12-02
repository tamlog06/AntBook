import sys
sys.setrecursionlimit(1000000)
from functools import lru_cache

def solve(Z, W):
    global X, Y
    X = Z
    Y = W
    ans = dfs(0, 0)
    return ans

@lru_cache(maxsize=None)
def dfs(i, count):
    global X, Y
    if i == N:
        return abs(X - Y)

    if count % 2 == 0:
        MAX = -float('inf')
        X_prev = X
        for j in range(i, N):
            X = a[j]
            MAX = max(MAX, dfs(j+1, count+1))
            X = X_prev
        return MAX
    else:
        MIN = float('inf')
        Y_prev = Y
        for j in range(i, N):
            Y = a[j]
            MIN = min(MIN, dfs(j+1, count+1))
            Y = Y_prev
        return MIN

def main():
    global N, a
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(Z, W))

if __name__ == '__main__':
    main()
