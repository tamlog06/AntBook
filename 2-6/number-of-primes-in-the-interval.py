def solve(a, b):
    is_prime_small = [True]*(int(b**0.5)+1)
    is_prime_small[0] = is_prime_small[1] = False
    is_prime = [True]*(b-a)

    for i in range(2, b):
        if i*i > b:
            break

        if is_prime_small[i]:
            for j in range(i*2, b+1, i):
                if j*j > b:
                    break
                is_prime_small[j] = False

            for j in range(max(2, (a+i-1)//i)*i, b+1, i):
                is_prime[j-a] = False

    return sum(is_prime)


def main():
    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == '__main__':
    main()

""" 入力例
22 37
"""

""" 出力例
3
"""

""" 入力例
22801763489 22801787297
"""

""" 出力例
1000
"""
