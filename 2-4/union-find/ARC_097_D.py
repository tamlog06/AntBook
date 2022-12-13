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

def solve(N, M, p, x, y):
    UF = UnionFind(N)
    for i in range(M):
        UF.union(x[i]-1, y[i]-1)


    ans = 0
    members = UF.all_group_members()
    for key, idxs in members.items():
        val = []
        for idx in idxs:
            val.append(p[idx]-1)

        ans += len(val) + len(idxs) - len(set(val + idxs))

    print(ans)

def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    x = []
    y = []
    for _ in range(M):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    solve(N, M, p, x, y)

if __name__ == '__main__':
    main()
