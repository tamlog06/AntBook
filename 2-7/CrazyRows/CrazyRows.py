def solve(N, A):
    a = [-1]*N
    for i in range(N):
        for j in range(N-1, -1, -1):
            if A[i][j] == 1:
                a[i] = j
                break

    res = 0
    for i in range(N):
        pos = -1
        for j in range(i, N):
            if a[j] <= i:
                pos = j
                break

        for j in range(pos, i, -1):
            a[j], a[j-1] = a[j-1], a[j]
            res += 1

    return res

def main():
    N = int(input())
    A = list(list(map(int, input().split())) for _ in range(N))
    print(A)
    print(solve(N, A))

if __name__ == '__main__':
    main()

""" 入力例
2
1 0
1 1
"""

""" 出力例
0
"""

""" 入力例
3
0 0 1
1 0 0
0 1 0
"""

""" 出力例
2
"""

""" 入力例
4
1 1 1 0
1 1 0 0
1 1 0 0
1 0 0 0
"""

""" 出力例
4
"""
