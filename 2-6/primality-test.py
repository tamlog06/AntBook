def is_prime(n):
    for i in range(2, n):
        if i*i > n:
            break

        if n%i == 0:
            return False

    return n != 1

def divisor(n):
    res = []
    for i in range(1, n+1):
        if i*i > n:
            break

        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)

    res.sort()
    return res

def prime_factor(n):
    res = {}
    for i in range(2, n+1):
        if i*i > n:
            break

        if n%i == 0:
            res[i] = 0
            while n%i == 0:
                n //= i
                res[i] += 1

    if n != 1:
        res[n] = 1

    return res


def solve(n):
    if n == 1:
        return 'No'
    elif n == 2:
        return 'Yes'
    
    for i in range(2, n):
        if i*i > n:
            break

        if n%i == 0:
            return 'No'

    return 'Yes'

def main():
    n = int(input())
    print(solve(n))
    print(is_prime(n))
    print(divisor(n))
    print(prime_factor(n))

if __name__ == '__main__':
    main()

""" 入力例
53
"""

""" 出力例
Yes
"""

""" 入力例
295927
"""

""" 出力例
No
"""
