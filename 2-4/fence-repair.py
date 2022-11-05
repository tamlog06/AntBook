def solve(N, L):
    import heapq
    # 最大のものを取り出し、ループの回数分足していく。本と逆の操作。
    L = [-x for x in L]
    heapq.heapify(L)
    ans = 0
    i = 0

    while len(L) > 2:
        i += 1
        ans += (-i)*heapq.heappop(L)

    ans += (-i-1)*sum(L)
    return ans

def main():
    N = int(input())
    L = list(map(int, input().split()))
    print(solve(N, L))

if __name__ == '__main__':
    main()

""" 入力例
3
8 5 8
"""

""" 出力例
34
"""
