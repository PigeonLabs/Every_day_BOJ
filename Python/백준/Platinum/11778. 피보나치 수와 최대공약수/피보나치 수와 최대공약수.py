import sys
input = sys.stdin.readline
from functools import cache

MOD = 1_000_000_007

@cache
def fib_fast_doubling(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_fast_doubling(n // 2)
        c = (a * ((2 * b - a) % MOD)) % MOD
        d = (a * a + b * b) % MOD
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % MOD)
        
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = list(map(int, input().split()))
print(fib_fast_doubling(gcd(x[0], x[1]))[0] % MOD)