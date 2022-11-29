from functools import lru_cache
# lru_cacheを使ってメモ化して高速化
def solve():
    field = '*'*9
    chokudai = dfs(field, 0)
    chokuko = sum([sum(b[i]) for i in range(2)]) + sum([sum(c[i]) for i in range(3)]) - chokudai
    return chokudai, chokuko

@lru_cache(maxsize=None)
def dfs(field, count):
    if count == 9:
        return score(field)

    if count % 2 == 0:
        MAX = -float('inf')
        for i in range(9):
            if field[i] == '*':
                field = field[:i] + 'o' + field[i+1:]
                MAX = max(MAX, dfs(field, count+1))
                field = field[:i] + '*' + field[i+1:]
        return MAX
    else:
        MIN = float('inf')
        for i in range(9):
            if field[i] == '*':
                field = field[:i] + 'x' + field[i+1:]
                MIN = min(MIN, dfs(field, count+1))
                field = field[:i] + '*' + field[i+1:]
        return MIN

def score(field):
    maze = [field[:3], field[3:6], field[6:]]
    val = 0
    for i in range(2):
        for j in range(3):
            if maze[i][j] == maze[i+1][j]:
                val += b[i][j]

    for i in range(3):
        for j in range(2):
            if maze[i][j] == maze[i][j+1]:
                val += c[i][j]

    return val

def main():
    global b, c
    b = [list(map(int, input().split())) for _ in range(2)]
    c = [list(map(int, input().split())) for _ in range(3)]
    ans = solve()
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
