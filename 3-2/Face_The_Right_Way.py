def solve(N, S):
    direction = []
    for s in S:
        if s == 'B':
            direction.append(1)
        else:
            direction.append(0)

    M_min = float('inf')
    K_min = float('inf')

    for K in range(1, N+1):
        M = calc(K, direction, N)
        if M_min > M:
            M_min = M
            K_min = K

    return K_min, M_min

def calc(K, direction, N):
    f = [0] * len(direction)
    res = 0
    S = 0

    for i in range(N-K+1):
        if (direction[i] + S) % 2 == 1:
            f[i] = 1
            res += 1

        S += f[i]
        if i-K+1 >= 0:
            S -= f[i-K+1]

    for i in range(N-K+1, N):
        if (direction[i] + S) % 2 == 1:
            return float('inf')

        S += f[i]
        if i-K+1 >= 0:
            S -= f[i-K+1]

    return res

def main():
    N = int(input())
    S = input()

    K, M = solve(N, S)
    print(K)
    print(M)


if __name__ == '__main__':
    main()

""" 入力例
7
BBFBFBB
"""

""" 出力例
3
3
"""
