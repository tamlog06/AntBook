n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
W = int(input())

w1, w2 = w[:n//2], w[n//2:]
v1, v2 = v[:n//2], v[n//2:]

ps = []
for i in range(2**len(w1)):
    weight = 0
    value = 0
    for j in range(len(w1)):
        if (i >> j) & 1:
            weight += w1[j]
            value += v1[j]
    ps.append((weight, value))

ps.sort(key=lambda x: [x[0], -x[1]])

m = 1
for i in range(1, len(ps)):
    if ps[m-1][1] < ps[i][1]:
        ps[m] = ps[i]
        m += 1

import bisect
res = 0
for i in range(2**len(w2)):
    weight = 0
    value = 0
    for j in range(len(w2)):
        if (i >> j) & 1:
            weight += w2[j]
            value += v2[j]

    if weight < W:
        idx = bisect.bisect_left(ps[:m], (W-weight, float('inf'))) - 1
        res = max(res, value + ps[idx][1])

print(res)

