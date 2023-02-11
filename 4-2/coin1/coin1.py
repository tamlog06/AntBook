from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

x = int(input())
k = int(input())
a = list(map(int, input().split()))

a.sort()

# coinの枚数がn
@lru_cache(maxsize=None)
def dfs(n):
    # if n == 1:
        # return True

    for i in range(k-1, -1, -1):
        if a[i] > n:
            continue
        elif a[i] == n:
            return True
        else:
            if not dfs(n - a[i]):
                return True

    return False

if dfs(x):
    print("Alice")
else:
    print("Bob")


# solver 2
win = [False] * (x + 1)
win[0] = False

for j in range(1, x+1):
    win[j] = False
    for i in range(k):
        if a[i] > j:
            break
        if not win[j - a[i]]:
            win[j] = True
            break

if win[x]:
    print("Alice")
else:
    print("Bob")


""" 入力例1
9
2
1 4
"""

""" 出力例1
Alice
"""

""" 入力例2
10
2
1 4
"""

""" 出力例2
Bob
"""
