def solve(n):
    coins = [500, 100, 50, 10, 5, 1]
    ans = 0
    n = 1000 - n
    for coin in coins:
        ans += n // coin
        n %= coin

    return ans

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
