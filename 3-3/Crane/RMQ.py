N, q = map(int, input().split())
com, x, y = [], [], []
for _ in range(q):
    c, a, b = map(int, input().split())
    com.append(c)
    x.append(a)
    y.append(b)


# N0 = 2**(N-1).bit_length()
N0 = 1
while N0 < N:
    N0 *= 2

INF = 2**31-1
# 1-indexed
data = [INF]*(2*N0)

# for i in range(N):
    # data[i+N0] = x[i]

# for i in range(N0-1, -1, -1):
    # data[i] = min(data[2*i], data[2*i+1])

# a_k の値を x に更新
def update(k, x):
    k += N0
    data[k] = x
    while k > 1:
        k = k // 2
        data[k] = min(data[2*k], data[2*k+1])

# 区間[l, r)の最小値
def query(l, r):
    L = l + N0
    R = r + N0

    s = INF
    while L < R:
        if R % 2 == 1:
            s = min(s, data[R-1])
            R -= 1

        if L % 2 == 1:
            s = min(s, data[L])
            L += 1

        L = L // 2
        R = R // 2
    return s



for i in range(q):
    if com[i] == 0:
        update(x[i], y[i])
    else:
        print(query(x[i], y[i]+1))
