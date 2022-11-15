def solve(N, w):
    ans = 1
    weights = [w[0]]
    for i in range(1, N):
        flag = True
        for j in range(len(weights)):
            if weights[j] >= w[i]:
                weights[j] = w[i]
                flag = False
                break

        if flag:
            weights.append(w[i])
            ans += 1

        weights.sort()

    return ans

    

def main():
    N = int(input())
    w = list(int(input()) for i in range(N))

    print(solve(N, w))

if __name__ == '__main__':
    main()
