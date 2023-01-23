class RMQ:
    def __init__(self, N, x):
        # N: 配列の要素数
        self.N = N

        n = 1
        while n < N:
            n *= 2

        self.dat = [float("inf")] * (2 * n - 1)

        for i in range(N):
            self.dat[i + N - 1] = x[i]

        for i in range(N - 2, -1, -1):
            self.dat[i] = min(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    # 0-indexed
    def update(self, k, a):
        # k: 更新する要素の添字
        # a: 更新する値

        k += self.N - 1
        self.dat[k] = a

        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, a, b, k, l, r):
        # [a, b)の最小値を求める
        # k: 現在見ているノードの添字
        # l, r: 現在見ているノードが[l, r)に対応していることを表す

        if r <= a or b <= l:
            return float("inf")

        if a <= l and r <= b:
            return self.dat[k]

        vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)

        return min(vl, vr)

if __name__ == '__main__':
    x = [5, 3, 7, 9, 6, 4, 1, 2]

    rmq = RMQ(len(x), x)

    print(rmq.dat)
    print(rmq.query(0, 7, 0, 0, rmq.N))

    rmq.update(0, 2)
    print(rmq.query(0, 4, 0, 0, rmq.N))
