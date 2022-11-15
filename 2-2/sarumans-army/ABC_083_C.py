def solve(X, Y):
    ans = 0
    while X <= Y:
        ans += 1
        X *= 2

    return ans

def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))

if __name__ == '__main__':
    main()
