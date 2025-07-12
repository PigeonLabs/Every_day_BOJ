from math import comb
n,r = map(int,input().split())
print(comb(n+r-1,r-1)%10**9)