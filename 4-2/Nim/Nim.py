N = int(input())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    xor ^= A[i]

if xor == 0:
    print("Bob")
else:
    print("Alice")

"""入力例１
3
1 2 4
"""

"""出力例１
Alice
"""

"""入力例２
3
1 2 3
"""

"""出力例２
Bob
"""
