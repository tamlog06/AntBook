V = int(input())
E = int(input())
G = [[] for _ in range(V)]
rG = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    rG[v].append(u)

vs = []

def dfs(v):
    used[v] = True
    for i in range(len(G[v])):
        if not used[G[v][i]]:
            dfs(G[v][i])
    # 番号を付けた順に頂点を格納する
    vs.append(v)


# 属する強連結成分のトポロジカル順序
cmp = [0] * V
def rdfs(v, k):
    used[v] = True
    cmp[v] = k

    for i in range(len(rG[v])):
        if not used[rG[v][i]]:
            rdfs(rG[v][i], k)


used = [False] * V
for v in range(V):
    if not used[v]:
        dfs(v)

used = [False] * V
k = 0
for i in range(len(vs)-1, -1, -1):
    if not used[vs[i]]:
        rdfs(vs[i], k)
        k += 1

# 強連結成分の数
print(k)
