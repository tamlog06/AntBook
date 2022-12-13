import sys, os
sys.path.append(os.path.join('..', 'utils'))
from UnionFind import UnionFind

def solve(N, M, edges):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(N)

    res = 0
    for i in range(M):
        e = edges[i]
        if not uf.same(e[0], e[1]):
            uf.union(e[0], e[1])
            res += e[2]

    return res


def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    print(solve(N, M, edges))

if __name__ == '__main__':
    main()

""" 入力例
7 9
0 1 10
0 3 2
2 3 1
3 4 7
1 4 5
3 5 3
4 5 1
4 6 8
5 6 5
"""

""" 出力例
17
"""
