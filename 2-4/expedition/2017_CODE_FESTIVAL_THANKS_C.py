import heapq
def solve(N, K, a, b):
    T = list(zip(a, [i for i in range(N)]))
    heapq.heapify(T)
    time = 0
    for i in range(K):
        t, i = heapq.heappop(T)
        time += t
        heapq.heappush(T, (t + b[i], i))

    return time

def main():
    N, K = map(int, input().split())
    a, b = [], []
    for _ in range(N):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)

    print(solve(N, K, a, b))

if __name__ == '__main__':
    main()

