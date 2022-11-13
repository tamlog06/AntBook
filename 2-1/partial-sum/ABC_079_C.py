def solve(S):
    ans = dfs(S, 0)
    return ans

def dfs(S, index):
    if index == 6:
        if eval(S) == 7:
            return True, S + '=7'
        else:
            return False, None

    plus = S[:index+1] + '+' + S[index+1:]
    minus = S[:index+1] + '-' + S[index+1:]

    ret, ans = dfs(plus, index+2)
    if ret:
        return True, ans

    ret, ans = dfs(minus, index+2)
    if ret:
        return True, dfs(minus, index+2)[1]

    return False, None

def main():
    S = input()
    print(solve(S)[1])

if __name__ == '__main__':
    main()
