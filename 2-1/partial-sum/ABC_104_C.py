import math
# def solve(D, G, p, c):
    # g = G//100 + 1
    # dp = [[float('inf') for _ in range(g)] for __ in range(D+1)]
    # p = [0] + p
    # c = [0] + c

    # for i in range(D+1):
        # c[i] = c[i] // 100

    # for i in range(g):
        # if i <= p[1]:
            # dp[1][i] = i
        # elif i <= p[1] + c[1]:
            # dp[1][i] = p[1]
        # else:
            # break

    # for i in range(2, D+1):
        # for j in range(g):
            # res = dp[i-1][j]
            # point = 1
            # while j - point >= 0:
                # if point <= p[i]*i:
                    # res = min(res, dp[i-1][j-point] + math.ceil(point/i))
                # elif point <= p[i]*i + c[i]:
                    # res = min(res, dp[i-1][j-point] + p[i])
                # else:
                    # break

                # point += 1

            # dp[i][j] = res

    # return dp[D][g-1]

import sys
sys.setrecursionlimit(100000000)

def solve():
    global ans
    ans = float('inf')
    # remain = [i for i in range(D)]
    haiten = []
    for i in range(D):
        haiten.append([(i+1)*p[i], i])
    haiten.sort(key=lambda x: x[0])

    sum = 0
    count = 0
    i = 0
    return(dfs(haiten, sum, count, i))

def dfs(remain, sum, count, i):
    global ans
    if i == D:
        # p_max = remain[-1]
        if remain == []:
            if sum >= G:
                ans = min(ans, count)
            return

        p_max = remain[-1][1]

        # for j in remain:
            # if p_max
        n = math.ceil((G-sum) / (p_max+1))
        n = max(0, n)
        if n <= p[p_max]:
            ans = min(ans, count+n)
        return

    dfs(remain, sum, count, i+1)
    dfs(remain[:i]+remain[i+1:], sum+(i+1)*p[i]+c[i], count+p[i], i+1)

    return ans


def main():
    global D, G, p, c
    D, G = map(int, input().split())
    G = G // 100
    p = []
    c = []
    for i in range(D):
        a, b = map(int, input().split())
        b //= 100
        p.append(a)
        c.append(b)

    print(solve())

if __name__ == '__main__':
    main()
