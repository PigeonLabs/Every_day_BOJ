import sys
sys.setrecursionlimit(10**8)
from functools import cache
MOD = 10**9

@cache
def fib_pair(n):
    if n == 0:
        return (0,1)
    a, b = fib_pair(n//2)
    c = a * ((b<<1)-a) % MOD
    d = (a*a + b*b) % MOD
    if n % 2 == 0:
        return c,d
    else:
        return d,(c+d) % MOD

a,b = map(int, input().split())
print((fib_pair(b+2)[0] - fib_pair(a+1)[0]) % MOD)