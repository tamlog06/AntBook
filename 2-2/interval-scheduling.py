def solve(n, s, t):
    ans = 0
    time = sorted(zip(s, t), key=lambda x: x[1])
    end = 0

    for i in range(n):
        if end <= time[i][0]:
            end = time[i][1]
            ans += 1
    return ans

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(solve(n, s, t))

if __name__ == '__main__':
    main()


""" 入力例
5
1 2 4 6 8
3 5 7 9 10
"""

""" 出力例
3
"""
