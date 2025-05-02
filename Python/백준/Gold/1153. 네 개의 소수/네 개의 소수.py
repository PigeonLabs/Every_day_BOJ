def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * len(range(i * i, n + 1, i))
    return sieve

n = int(input())
if n < 8:
    print(-1)
    exit()

is_prime = get_primes(n)

if n % 2 == 0:
    base = [2, 2]
    target = n - 4
else:
    base = [2, 3]
    target = n - 5

for i in range(2, target // 2 + 1):
    if is_prime[i] and is_prime[target - i]:
        print(*sorted(base + [i, target - i]))
        break