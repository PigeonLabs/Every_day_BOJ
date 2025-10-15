import math

MOD = 1_000_000_007

n = int(input())
a,b = map(int, input().split())

p = (n * n - 1) * (b - a) ** 3
q = 6 * (n * n)

g = math.gcd(p, q)
p //= g
q //= g

print(p * pow(q, MOD - 2, MOD) % MOD)