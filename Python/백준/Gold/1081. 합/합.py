def block(k):
    if k == 0:
        return 0
    return k * 45 * (10 ** (k - 1))

def calc(n):
    if n < 10:
        return n * (n + 1) // 2

    s = str(n)
    length = len(s)
    p = 10 ** (length - 1)
    d = n // p
    lo = n % p

    return d * block(length - 1) + (d * (d - 1) // 2) * p + d * (lo + 1) + calc(lo)

L,U = map(int,input().split())
print(calc(U) - calc(L-1) if L>0 else calc(U))