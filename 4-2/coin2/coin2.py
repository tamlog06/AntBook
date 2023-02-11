n = int(input())
k = int(input())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

max_x = max(x)
grundy = [0] * (max_x + 1)

def mex(s):
    i = 0
    # set型は"in"が定数オーダーで可能
    while i in s:
        i += 1
    return i

for j in range(1, max_x+1):
    s = set()
    for i in range(k):
        if a[i] <= j:
            s.add(grundy[j-a[i]])

    grundy[j] = mex(s)

xor = 0
for i in range(n):
    xor ^= grundy[x[i]]

if xor == 0:
    print("Bob")
else:
    print("Alice")

"""入力例１
3
3
1 3 4
5 6 7
"""

"""出力例１
Alice
"""

"""入力例２
3
3
1 3 4
5 6 8
"""

"""出力例２
Bob
"""
