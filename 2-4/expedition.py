def solve(N, L, P, A, B):
    import heapq
    # 問題文にはAがソートされていると書いていないので、小さい順にソートする必要がある
    A.append(L)
    B.append(0)

    A, B = zip(*sorted(zip(A, B), key=lambda x: x[0]))
    que = []
    ans = 0
    pos = 0
    for i in range(N):
        P -= (A[i] - pos)
        pos = A[i]

        heapq.heappush(que, -B[i])

        while P <= 0:
            if len(que) == 0:
                return -1

            P += heapq.heappop(que)*(-1)
            ans += 1

    return ans

def main():
    N, L, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(solve(N, L, P, A, B))

if __name__ == '__main__':
    main()


""" 入力例
4 25 10
14 20 10 21
5 2 10 4
"""

""" 出力例
2
"""
