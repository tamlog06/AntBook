def solve(n):
    return sieve(n)

def sieve(n):
    p = 0
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            p += 1
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    return p

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()

""" 入力例
11
"""

""" 出力例
5
"""

""" 入力例
1000000
"""

""" 出力例
78498
"""
