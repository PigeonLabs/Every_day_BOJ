from functools import cache

@cache
def t(n):
    if n == 0:
        return 1
    res = 0
    for i in range(0, n):
        res += t(i)*t(n-1-i)
    return res

n = int(input())
print(t(n))