def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

count = 0
a,b = map(int, input().split())
for i in prime_numbers(int(b**.5)):
    x = i*i
    while x <= b:
        if x >= a:
            count += 1
        x *= i
print(count)