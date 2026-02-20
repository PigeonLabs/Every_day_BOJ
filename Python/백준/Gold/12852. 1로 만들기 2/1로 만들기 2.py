n = int(input())

arr = [0] * (n+1)
p = [0] * (n+1)

arr[1] = 0
p[1] = 0

for i in range(2, n+1):
    arr[i] = arr[i-1] + 1
    p[i] = i-1
    if i % 2 == 0 and arr[i] > arr[i // 2] + 1:
        arr[i] = arr[i//2] + 1
        p[i] = i//2
    if i % 3 == 0 and arr[i] > arr[i // 3] + 1:
        arr[i] = arr[i//3] + 1
        p[i] = i//3

print(arr[n])
c = n
while c != 0:
    print(c, end=' ')
    if c == 1:
        break
    c = p[c]