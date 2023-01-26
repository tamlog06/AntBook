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


def solve(N, a):
    BIT_ = BIT(N)
    ans = 0

    for i in range(N):
        BIT_.add(a[i], 1)
        ans += i + 1 - BIT_.sum(a[i])

    return ans

def main():
    N = int(input())
    a = list(map(int, input().split()))

    print(solve(N, a))

if __name__ == '__main__':
    main()
