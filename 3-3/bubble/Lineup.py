class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


def solve(N, H):
    BIT_ = BIT(N)
    ans = 0

    sorted_H = sorted(H)
    order = {sorted_H[i]: i + 1 for i in range(N)}

    from collections import defaultdict
    see = defaultdict(bool)
    for i in range(N):
        if see[H[i]]:
            return -1
        
        see[H[i]] = True
        BIT_.add(order[H[i]], 1)
        ans += (i + 1 - BIT_.sum(order[H[i]]))*H[i]

    return ans


def main():
    N = int(input())
    H = list(map(int, input().split()))

    print(solve(N, H))

if __name__ == '__main__':
    main()
