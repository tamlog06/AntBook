import heapq
def solve(N, a):
    b = a[:N]
    c = [-a[i] for i in range(2*N, 3*N)]

    b_sum = sum(b)
    c_sum = -sum(c)
    
    heapq.heapify(b)
    heapq.heapify(c)

    b_max = [0 for _ in range(N+1)]
    c_min = [0 for _ in range(N+1)]

    b_max[0] = b_sum
    c_min[-1] = c_sum

    for i in range(N):
        heapq.heappush(b, a[N+i])
        heapq.heappush(c, -a[2*N-i-1])

        b_ = heapq.heappop(b)
        c_ = -heapq.heappop(c)

        b_sum += a[N+i] - b_
        c_sum += a[2*N-i-1] - c_

        b_max[i+1] = b_sum
        c_min[-i-2] = c_sum

    ans = -float('inf')

    for i in range(N+1):
        ans = max(ans, b_max[i] - c_min[i])

    return ans


def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(solve(N, a))

if __name__ == '__main__':
    main()
