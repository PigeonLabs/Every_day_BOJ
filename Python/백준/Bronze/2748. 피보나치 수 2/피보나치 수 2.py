from functools import cache

@cache
def fib(n):
    if n==0:
        return 0
    elif n<3:
        return 1
    return fib(n-2)+fib(n-1)

print(fib(int(input())))