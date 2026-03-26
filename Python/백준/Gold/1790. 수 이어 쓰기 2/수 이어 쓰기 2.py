n, k = map(int, input().split())

length = 1
count = 9
start = 1

while k > length * count:
    k -= length * count
    length += 1
    count *= 10
    start *= 10

num = start + (k - 1) // length
idx = (k - 1) % length

if num > n:
    print(-1)
else:
    print(str(num)[idx])