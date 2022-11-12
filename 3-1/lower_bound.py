def solve(n, a, k):
    lower = -1
    upper = n

    while upper - lower > 1:
        mid = (lower+upper)//2
        if a[mid] >= k:
            upper = mid
        else:
            lower = mid


    return upper

def solve_bisec(n, a, k):
    import bisect

    return bisect.bisect_left(a, k)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(solve(n, a, k))
    print(solve_bisec(n, a, k))

if __name__ == '__main__':
    main()

""" 入力例
5
2 3 3 5 6
3
"""

""" 出力例
1
"""
