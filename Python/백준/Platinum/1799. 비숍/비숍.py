import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

blk,wte = [],[]
for y in range(n):
    for x in range(n):
        if arr[y][x] == 1:
            ((blk if (y + x) % 2 == 0 else wte)).append((y, x))

def solve(cells):
    diaglr, diagrl = set(), set()
    res = 0

    def dfs(idx, count):
        nonlocal res
        if idx == len(cells):
            res = max(res, count)
            return
        y, x = cells[idx]
        if (y - x) not in diaglr and (y + x) not in diagrl:
            diaglr.add(y - x)
            diagrl.add(y + x)
            dfs(idx + 1, count + 1)
            diaglr.remove(y - x)
            diagrl.remove(y + x)
        dfs(idx + 1, count)

    dfs(0, 0)
    return res

res = solve(blk) + solve(wte)
print(res)