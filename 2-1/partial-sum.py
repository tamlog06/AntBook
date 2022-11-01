def solve(i, s, n, a, k):
    if i == n:
        return s == k
    
    # iの要素を使わない場合
    elif solve(i+1, s, n, a, k):
        return True
    # iの要素を使う場合
    elif solve(i+1, s+a[i], n, a, k):
        return True

    return False

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    ans = solve(0, 0, n, a, k)
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

""" 入力例 1
4
1 2 4 7
13
"""

""" 出力例 1
Yes
"""

""" 入力例 2
4
1 2 4 7
15
"""

""" 出力例 2
No
"""
