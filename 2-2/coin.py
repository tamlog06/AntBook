def solve(C, A):
    ans = 0
    coin = [1, 5, 10, 50, 100, 500]
    for i in range(5, -1, -1):
        t = min(A // coin[i], C[i])
        ans += t
        A -= t * coin[i]
    return ans

def main():
    C = list(map(int, input().split()))
    A = int(input())
    print(solve(C, A))

if __name__ == '__main__':
    main()

""" 入力例
3 2 1 3 0 2
620
"""

""" 出力例
6
"""
