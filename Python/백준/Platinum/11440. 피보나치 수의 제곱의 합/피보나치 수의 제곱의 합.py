import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def fib(n):
    if n == 0:
        return (0, 1)
    a, b = fib(n // 2)
    c = (a * ((2 * b - a) % MOD)) % MOD
    d = (a * a + b * b) % MOD
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)

n = int(input())
print(fib(n)[0] * fib(n)[1] % MOD)