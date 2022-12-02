from collections import defaultdict
def solve(N, s, M, t):
    d_b = defaultdict(int)
    d_r = defaultdict(int)

    keys = []
    for b in s:
        d_b[b] += 1
        keys.append(b)

    for r in t:
        d_r[r] += 1

    keys = set(keys)

    ans = 0
    for key in keys:
        ans = max(ans, d_b[key] - d_r[key])

    return ans

def main():
    N = int(input())
    s = list(input() for _ in range(N))
    M = int(input())
    t = list(input() for _ in range(M))
    print(solve(N, s, M, t))

if __name__ == '__main__':
    main()
