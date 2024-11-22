def hanoi(s, to, e, n):
    if n == 1:
        print(s, e)
        return
    if n <= 20:
        hanoi(s, e, to, n-1)
        print(s, e)
        hanoi(to, s, e, n-1)

n = int(input())
print(2**n - 1)
hanoi(1, 2, 3, n)