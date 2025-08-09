import sys,math
input = sys.stdin.readline

def solve(a,b):
    D = b - a
    if D <= 0:
        return 0
    s = math.isqrt(1 + 4*D)
    n = (s - 1) // 2
    if n * (n + 1) > D:
        n -= 1
    return n

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    x = solve(a, b)
    t = (b-a)-x*(x+1)
    if t == 0:
        print(2*x)
    elif t<=x+1:
        print(2*x+1)
    else:
        print(2*x+2)