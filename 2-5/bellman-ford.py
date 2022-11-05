def solve(n, e, s, g):
    d = [float('inf')]*n
    d[s] = 0

    # while True:
    for _ in range(n):
        if _ == n-1:
            # もしV-1回目のループで更新があったら負の閉路が存在する
            return -1

        update = False

        for i in range(len(e)):
            v_from, v_to, cost = e[i]
            if d[v_from] != float('inf') and d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost
                update = True

            if d[v_to] != float('inf') and d[v_from] > d[v_to] + cost:
                d[v_from] = d[v_to] + cost
                update = True

        if not update:
            break

    print(d)
    return d[g]

def main():
    n, e = map(int, input().split())
    s, g = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    # v = [[-1]*n for _ in range(n)]
    # for x, y, z in edges:
        # v[x][y] = z
        # v[y][x] = z

    print(solve(n, edges, s, g))

if __name__ == '__main__':
    main()

""" 入力例
7 10
0 6
0 1 2
0 2 5
1 2 4
1 3 6
2 3 2
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9
"""

""" 出力例
16
"""


