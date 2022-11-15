def solve(N, LR):
    LR.sort(key=lambda x: x[1])

    ans = 0
    last = -float('inf')
    for l, r in LR:
        if l >= last:
            ans += 1
            last = r

    return ans

def main():
    N = int(input())
    X, L = [], []
    LR = []
    for _ in range(N):
        x, l = map(int, input().split())
        LR.append((x-l, x+l))

    print(solve(N, LR))

if __name__ == '__main__':
    main()
