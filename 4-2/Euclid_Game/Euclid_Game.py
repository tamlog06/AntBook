a, b = map(int, input().split())
if b > a:
    a, b = b, a

flag = True
while b != 0:
    if b > a:
        a, b = b, a

    if a % b == 0:
        break

    if a - b > b:
        break

    a -= b
    flag = not flag

if flag:
    print("Stan wins")
else:
    print("Ollie wins")



""" 入力例１
34 12
"""

""" 出力例１
Stan wins
"""

""" 入力例２
15 24
"""

""" 出力例２
Ollie wins
"""
