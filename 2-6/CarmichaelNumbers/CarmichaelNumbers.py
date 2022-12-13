def is_prime(n):
    for i in range(2, n):
        if i*i > n:
            break

        if n%i == 0:
            return False

    return True

def solve(n):
    if is_prime(n):
        return 'No'

    for x in range(2, n):
        if pow(x, n, n) != x:
            return 'No'
    return 'Yes'

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()

""" 入力例
17
"""

""" 出力例
No
"""

""" 入力例
561
"""

""" 出力例
Yes
"""

""" 入力例
4
"""

""" 出力例
No
"""
