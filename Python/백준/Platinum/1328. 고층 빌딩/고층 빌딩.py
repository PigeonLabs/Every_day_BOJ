import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

MOD = 1_000_000_007

n, l, r = map(int, input().split())

from functools import cache

@cache
def solve(x, xl, xr):
    if xl <= 0 or xr <= 0 or xl > x or xr > x:
        return 0
    if x == 1:
        return 1 if (xl == 1 and xr == 1) else 0
    return (solve(x-1, xl-1, xr) + solve(x-1, xl, xr-1) + (x-2) * solve(x-1, xl, xr)) % MOD

print(solve(n, l, r))