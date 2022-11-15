def solve(S, T):
    ans = ""
    for i in range(len(S)-len(T)+1):
        if S[i] == T[0] or S[i] == '?':
            flag = True
            for j in range(len(T)):
                if S[i+j] != T[j] and S[i+j] != '?':
                    flag = False
                    break
            
            if not flag:
                continue

            S_ans = S[:i] + T + S[i+len(T):]
            S_ans = toS(S_ans)
            if ans == '':
                ans = S_ans
            else:
                ans = min(ans, S_ans)

    if ans == '':
        return 'UNRESTORABLE'
    else:
        return ans

def toS(S):
    ans = ''
    for s in S:
        if s == '?':
            ans += 'a'
        else:
            ans += s
    return ans

def main():
    S = input()
    T = input()
    print(solve(S, T))

if __name__ == '__main__':
    main()
