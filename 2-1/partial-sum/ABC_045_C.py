def solve(S):
    ans = dfs(S, 0)
    return ans

def dfs(S, index):
    ret = 0
    if index == len(S)-1:
        return eval(S)

    ret += dfs(S, index+1)
    plus = S[:index+1] + '+' + S[index+1:]
    ret += dfs(plus, index+2)

    return ret

def main():
    S = input()
    print(solve(S))

if __name__ == '__main__':
    main()
