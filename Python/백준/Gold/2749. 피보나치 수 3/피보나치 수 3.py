n = int(input())%1500000
fib = [0, 1]
for i in range(2, n + 1):
    fib.append((fib[i - 1] + fib[i - 2]) % 1000000)
print(fib[-1])