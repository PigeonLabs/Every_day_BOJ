def maxfib(n):
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return a

n = int(input())

while True:
    f = maxfib(n)
    if f == n:
        print(n)
        break
    n -= f