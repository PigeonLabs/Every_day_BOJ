n, a, b = [x - 1 for x in map(int, input().split())]

i = 0
while n>=2**i:
    i += 1

for k in range(i):
    if a//2**(i-k-1) != b//2**(i-k-1):
        print(i-k)
        exit()