def solve(N, d):
    return len(set(d))

def main():
    N = int(input())
    d = list(int(input()) for _ in range(N))
    print(solve(N, d))

if __name__ == '__main__':
    main()
