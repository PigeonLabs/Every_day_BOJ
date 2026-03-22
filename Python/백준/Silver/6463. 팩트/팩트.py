import sys
input = sys.stdin.readline

res = [0, 1]
for i in range(2, 10001):
    t = res[-1] * i
    while t % 10 == 0:
        t //= 10
    t %= 100000
    res.append(t)

for line in sys.stdin:
    A = int(line)
    print(f"{A:>5} -> {res[A] % 10}")