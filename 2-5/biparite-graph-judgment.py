def dfs(v, c):
    global color, vertexes
    color[v] = c
    for n in vertexes[v]:
        if color[n] == c:
            return False
        if color[n] == 0 and not dfs(n, -c):
            return False

    return True

def solve(n, v):
    global color, vertexes
    vertexes = v
    color = [0]*n
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                return False

    return True

def main():
    n, e = map(int, input().split())
    edges = list(map(int, input().split()) for _ in range(e))
    v = [[] for _ in range(n)]
    for x, y in edges:
        v[x].append(y)
        v[y].append(x)

    if solve(n, v):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()


""" 入力例1
3 3
0 1
1 2
2 0
"""

""" 出力例1
No
"""

""" 入力例2
4 4
0 1
0 3
1 2
2 3
"""

""" 出力例2
Yes
"""
