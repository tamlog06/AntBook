import sys, os
sys.path.append(os.path.join('..', 'utils'))
from UnionFind import UnionFind

def solve(N, K, que):
    UF = UnionFind(N*3)
    ans = 0
    for a, b, c in que:
        b -= 1
        c -= 1

        if b < 0 or b >= N or c < 0 or c >= N:
            ans += 1
            continue

        if a == 1:
            if UF.same(b, c+N) or UF.same(b, c+N*2):
                ans += 1
            else:
                UF.union(b, c)
                UF.union(b+N, c+N)
                UF.union(b+N*2, c+N*2)
        else:
            if UF.same(b, c) or UF.same(b, c+N*2):
                ans += 1
            else:
                UF.union(b, c+N)
                UF.union(b+N, c+N*2)
                UF.union(b+N*2, c)

    return ans
            

def main():
    N, K = map(int, input().split())
    que = [list(map(int, input().split())) for _ in range(K)]
    print(solve(N, K, que))

if __name__ == '__main__':
    main()

""" 入力例
100 7
1 101 1
2 1 2
2 2 3
2 3 3
1 1 3
2 3 1
1 5 5
"""

""" 出力例
3
"""
