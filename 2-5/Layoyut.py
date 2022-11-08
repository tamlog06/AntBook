def solve(n, A, B):
    d = [float('inf')]*(n+1)
    d[1] = 0

    for i in range(n):
        update = False

        for j in range(1, n):
            if d[j+1] != float('inf') and d[j] > d[j+1] + 0:
                update = True
                d[j] = d[j+1] + 0

        for fro, to, cost in A:
            if d[fro] != float('inf') and d[to] > d[fro] + cost:
                update = True
                d[to] = d[fro] + cost

        for to, fro, cost in B:
            if d[fro] != float('inf') and d[to] > d[fro] - cost:
                update = True
                d[to] = d[fro] - cost

        if update and i == n-1:
            return -2
        
        if not update:
            break

    if d[n] == float('inf'):
        return -1
    else:
        return d[n]


def main():
    N, ML, MD = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(ML)]
    B = [list(map(int, input().split())) for _ in range(MD)]
    print(solve(N, A, B))

if __name__ == '__main__':
    main()

""" 入力例
4 2 1
1 3 10
2 4 20
2 3 3
"""

""" 出力例
27
"""
