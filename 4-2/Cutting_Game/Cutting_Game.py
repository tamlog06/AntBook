W, H = map(int, input().split())

mem = [[-1]*(W+1) for _ in range(H+1)]

def grundy(w, h):
    if mem[h][w] != -1:
        return mem[h][w]

    s = set()
    for i in range(2, w-1):
        s.add(grundy(i, h) ^ grundy(w-i, h))

    for i in range(2, h-2):
        s.add(grundy(w, i) ^ grundy(w, h-i))

    mex = 0
    while mex in s:
        mex += 1

    mem[h][w] = mex
    return mex

if grundy(W, H) == 0:
    print("LOSE")
else:
    print("WIN")


"""入力例１
2 2
"""

"""出力例１
LOSE
"""

"""入力例２
4 2
"""

"""出力例２
WIN
"""
