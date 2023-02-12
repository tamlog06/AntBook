N = int(input())
M = int(input())
A, B = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

G = [[] for _ in range(N+1)]
rG = [[] for _ in range(N+1)]
for i in range(M):
    G[A[i]].append(B[i])
    rG[B[i]].append(A[i])

used = [False] * (N+1)
vs = []
def dfs(v):
    used[v] = True
    for u in G[v]:
        if not used[u]:
            dfs(u)
    vs.append(v)


cmp = [0] * (N+1)
def rdfs(v, k):
    used[v] = True
    cmp[v] = k
    for u in rG[v]:
        if not used[u]:
            rdfs(u, k)
    
used = [False] * (N+1)
for n in range(1, N+1):
    if not used[n]:
        dfs(n)

used = [False] * (N+1)
k = 0
for n in range(N-1, -1, -1):
    if not used[vs[n]]:
        rdfs(vs[n], k)
        k += 1

u = 0
num = 0
for v in range(1, N+1):
    if cmp[v] == k-1:
        u = v
        num += 1

used = [False] * (N+1)

rdfs(u, 0)

for v in range(1, N+1):
    if not used[v]:
        num = 0
        break

print(num)


"""入力例１
3
3
1 2
2 1
2 3
"""

"""出力例１
1
"""
