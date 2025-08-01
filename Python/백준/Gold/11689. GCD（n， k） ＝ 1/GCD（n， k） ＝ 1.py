import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = [False] * (((limit - p * p) // p) + 1)
    return [i for i, prime in enumerate(is_prime) if prime]

def prime_factors(n):
    fac = {}
    for p in sieve(int(math.isqrt(n))+1):
        if p*p > n:
            break
        while n % p == 0:
            fac[p] = fac.get(p, 0) + 1
            n //= p
    if n > 1:
        fac[n] = 1
    return fac

n = int(input())
res = n
for i in prime_factors(n):
    res -= res//i
print(res)