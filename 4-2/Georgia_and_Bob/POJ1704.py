N = int(input())
P = list(map(int, input().split()))

if N % 2 == 1:
    P = [0] + P

P.sort()

xor = 0
for i in range(0, len(P), 2):
    xor ^= (P[i+1] - P[i] - 1)

if xor == 0:
    print("Bob will win")
else:
    print("Georgia will win")


"""入力例１
3
1 2 3
"""

"""出力例１
Bob will win
"""

"""入力例２
8
1 5 6 7 9 12 14 17
"""

"""出力例２
Georgia will win
"""

