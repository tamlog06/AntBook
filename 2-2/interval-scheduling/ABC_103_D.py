def solve(N, M, ab):
    ab.sort(key=lambda x: x[1])

    ans = 0
    last = -float('inf')
    for a, b in ab:
        if a >= last:
            ans += 1
            last = b

    return ans


def main():
    N, M = map(int, input().split())
    ab = []
    for _ in range(M):
        a, b = map(int, input().split())
        ab.append((a, b))

    print(solve(N, M, ab))

if __name__ == '__main__':
    main()
