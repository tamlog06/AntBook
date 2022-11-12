# dp[i][j]: 最後にj番目の的に当てた時の最大得点として解いたが、これでは解けないことがわかった。
# def solve(N, M, P):
    # dp = [[0]*(N+1) for _ in range(4)]
    # P = [0] + P


    # for i in range(N+1):
        # if P[i] <= M:
            # # print(dp[0][i])
            # dp[0][i] = P[i]

    # for i in range(1, 4):
        # # print(dp[i-1])
        # for j in range(N+1):
            # res = 0
            # for k in range(N+1):

                # if res < dp[i-1][k] + P[j] <= M:
                    # res = dp[i-1][k] + P[j]

            # dp[i][j] = res

    # max_val = 0
    # for i in range(N+1):
        # max_val = max(max_val, dp[3][i])

    # return max_val

import bisect
def solve(N, M, P):
    P = [0] + P
    points = []
    for i in range(N+1):
        for j in range(N+1):
            point = P[i] + P[j]
            if point <= M:
                points.append(point)
    points.sort()

    max_val = 0
    for point in points:
        index = bisect.bisect_left(points, M-point)
        max_val = max(max_val, point + points[index-1])

    return max_val

def main():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(N)]
    print(solve(N, M, P))

if __name__ == '__main__':
    main()
