n,k = map(int,input().split())

i = 0
while bin(n).count('1') > k:
    n += 1
    i += 1

print(i)