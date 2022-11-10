def solve(n, v1, v2):
    v1.sort()
    v2.sort(reverse=True)

    return sum([v1[i]*v2[i] for i in range(n)])

def main():
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    print(solve(n, v1, v2))

if __name__ == '__main__':
    main()

""" 入力例
3
1 3 -5
-2 4 1
"""

""" 出力例
-25
"""

""" 入力例
5
1 2 3 4 5
1 0 1 0 1
"""

""" 出力例
6
"""
