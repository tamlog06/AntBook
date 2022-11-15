def solve(N, S):
    ans = ''
    start = 0
    end = N
    for _ in range(N):
        if S[start:end] < S[start:end][::-1]:
            ans += S[start]
            start += 1
        elif S[start:end] > S[start:end][::-1]:
            ans += S[end - 1]
            end -= 1
        else:
            ans += S[start]
            start += 1

    return ans

def main():
    N = int(input())
    S = input()
    print(solve(N, S))

if __name__ == '__main__':
    main()


""" 入力例
6
ACDBCB
"""

""" 出力例
ABCBCD
"""
