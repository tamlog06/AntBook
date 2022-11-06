import os, sys
sys.path.append(os.path.join('..', 'utils'))
from UnionFind import UnionFind

def solve(N, M, edges):
    uf = UnionFind(N+M)
    edges.sort(key=lambda x: x[2], reverse=True)

    ans = 10000*(N+M)

    for n, m, cost in edges:
        if not uf.same(n, m+N):
            ans -= cost
            uf.union(n, m+N)

    return ans


def main():
    N, M, R = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(R)]
    print(solve(N, M, edges))

if __name__ == '__main__':
    main()

""" 入力例１
5 5 8
4 3 6831
1 3 4583
0 0 6592
0 1 3063
3 3 4975
1 3 2049
4 2 2104
2 2 781
"""

""" 出力例１
71071
"""

""" 入力例２
5 5 10
2 4 9820
3 2 6236
3 1 8864
2 4 8326
2 0 5156
2 0 1463
4 1 2439
0 4 4373
3 4 8889
2 4 3133
"""

""" 出力例２
54223
"""
