n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

CD = []
for c in C:
    for d in D:
        CD.append(c+d)
CD.sort()

import bisect

ans = 0

for a in A:
    for b in B:
        ans += bisect.bisect_right(CD, -(a+b)) - bisect.bisect_left(CD, -(a+b))

print(ans)
