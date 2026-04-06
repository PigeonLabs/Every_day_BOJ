import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve(x, t, arr):
    if x == t:
        expr = ''.join(arr)
        if eval(expr.replace(' ', '')) == 0:
            print(expr)
        return

    nxt = str(x + 1)
    solve(x + 1, t, arr + [' '] + [nxt])
    solve(x + 1, t, arr + ['+'] + [nxt])
    solve(x + 1, t, arr + ['-'] + [nxt])

n = int(input())
for _ in range(n):
    t = int(input())
    solve(1, t, ['1'])
    print()