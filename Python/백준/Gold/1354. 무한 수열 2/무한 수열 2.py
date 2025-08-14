import sys
input = sys.stdin.readline
from functools import cache

n,p,q,x,y = map(int, input().split())

@cache
def solve(i):
    if i <= 0:
        return 1
    else:
        return solve(i//p-x)+solve(i//q-y)
    
print(solve(n))