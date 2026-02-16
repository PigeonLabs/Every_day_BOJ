import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def solve(y, x):
    if y == 0 and x == 0:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] > arr[y][x]:
            dp[y][x] += solve(ny, nx)

    return dp[y][x]

print(solve(m-1, n-1))