from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def solve(N, K, L, p, q, r, s):
    uf1 = UnionFind(N)
    uf2 = UnionFind(N)

    for i in range(K):
        uf1.union(p[i]-1, q[i]-1)

    for i in range(L):
        uf2.union(r[i]-1, s[i]-1)

    ans = [0] * N
    for i in range(N):
        uf1_members = uf1.members(i)
        uf2_members = uf2.members(i)
        members = set(uf1_members) & set(uf2_members)
        ans[i] = len(members)

    print(*ans)


def main():
    N, K, L = map(int, input().split())
    p = [0] * K
    q = [0] * K
    r = [0] * L
    s = [0] * L
    for i in range(K):
        p[i], q[i] = map(int, input().split())
    for i in range(L):
        r[i], s[i] = map(int, input().split())
    solve(N, K, L, p, q, r, s)

if __name__ == '__main__':
    main()
