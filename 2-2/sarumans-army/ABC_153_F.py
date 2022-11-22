# 累積和などを勉強してから再度解いてみよう
def solve(N, D, A, X, H):
    XH = sorted(zip(X, H), key=lambda x: x[0])
    X = [x for x, h in XH]
    H = [h for x, h in XH]

    ans = 0
    now_index = 0
    max_index = 0

    for i in range(N):
        if H[i] <= 0:
            continue

        now_index = i
        # max_index = i
        while max_index < N and X[max_index] - X[now_index] <= 2*D:
            max_index += 1

        cnt = -(-H[now_index] // A)
        for j in range(now_index, max_index):
            H[j] -= cnt * A
        ans += cnt

    return ans

def main():
    N, D, A = map(int, input().split())
    X = []
    H = []
    for _ in range(N):
        x, h = map(int, input().split())
        X.append(x)
        H.append(h)

    print(solve(N, D, A, X, H))

if __name__ == '__main__':
    main()

