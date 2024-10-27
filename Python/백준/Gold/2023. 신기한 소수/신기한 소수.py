from functools import cache

@cache
def is_prime_number(x):
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def append_digits(n):
    result = []
    for i in range(1,10,2):
        result.append(int(f"{n}{i}"))
    return result

def prime(n,r,arr):
    if n-1==r:
        for i in arr:
            print(i)
    else:
        arrn = []
        for i in arr:
            for j in append_digits(i):
                if is_prime_number(j):
                    arrn.append(j)
        prime(n+1,r,arrn)

r = int(input())
prime(2,r,[2,3,5,7])