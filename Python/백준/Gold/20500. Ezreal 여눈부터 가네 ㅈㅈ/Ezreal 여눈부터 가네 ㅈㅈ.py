import math

n = int(input())
res = 0
for f in range(1,n+1):
    if (f*5+(n-f))%3:
        continue
    res += math.comb(n-1,f-1)%(10**9+7)
print(res%(10**9+7))