# def solve(N, t):
    # import itertools

    # p = itertools.permutations(t)
    # ans = float('inf')

    # for v in p:
        # ans = min(ans, calc(v))

    # return ans

# def calc(v):
    # if len(v) == 1:
        # return v[0]

    # time = [v[0], v[1]]
    # ans = 0
    # # for i in range(2, len(v)):
    # i = 2
    # while i < len(v):
        # if time[0] > time[1]:
            # time[0] -= time[1]
            # ans += time[1]
            # time[1] = v[i]
            # i += 1
        # elif time[0] < time[1]:
            # time[1] -= time[0]
            # ans += time[0]
            # time[0] = v[i]
            # i += 1
        # else:
            # ans += time[0]
            # if i == len(v) - 1:
                # return ans + v[i]
            # else:
                # time[0] = v[i]
                # time[1] = v[i+1]

            # i += 2

    # return ans + max(time)

def solve(N, t):
    ans = float('inf')
    for i in range(2**N):
        time = [0, 0]
        for j in range(N):
            if (i >> j) & 1:
                time[0] += t[j]
            else:
                time[1] += t[j]

        ans = min(ans, max(time))

    return ans



def main():
    N = int(input())
    t = list(int(input()) for _ in range(N))
    print(solve(N, t))

if __name__ == '__main__':
    main()
