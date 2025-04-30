import math

def stirling(n,k):
    if n==0 and k==0:
        return 1
    elif n==0 or k==0:
        return 0
    return stirling(n-1,k-1)+(n-1)*stirling(n-1,k)

def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

n,m = map(int,input().split())
res = 0
for i in range(1,m+1):
    res += stirling(n,i)

d = math.gcd(res,math.factorial(n))
print(f"{res//d}/{math.factorial(n)//d}")