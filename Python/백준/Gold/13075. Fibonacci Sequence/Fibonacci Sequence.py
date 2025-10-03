import sys
input = sys.stdin.readline
from functools import cache

MOD = 10**9

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

n = int(input())
for _ in range(n):
    k = int(input()) % (15 * (10**8))
    print(fib_fast_doubling(k)[0])