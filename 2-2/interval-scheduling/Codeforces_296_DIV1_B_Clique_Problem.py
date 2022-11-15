def solve(N, ab):
    ab.sort(key=lambda x: x[1])

    ans = 0
    last = -float('inf')
    for a, b in ab:
        if a >= last:
            ans += 1
            last = b

    return ans

def main():
    N = int(input())
    ab = []
    for _ in range(N):
        x, w = map(int, input().split())
        ab.append((x-w, x+w))

    print(solve(N, ab))

if __name__ == '__main__':
    main()
