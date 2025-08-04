import math

n = int(input())
x = 1
while True:
    d = int(math.log10(x)) + 1
    if n <= d:
        print(str(x)[n - 1])
        break
    n -= d
    x += 1