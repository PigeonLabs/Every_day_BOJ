from math import gcd

def mul(res,a,b,c,d):
    lcm = res[a] * c // gcd(res[a], c)
    res[b] = lcm * d // c
    res[a] = lcm

n = int(input())
res = [1]*n
l = []
for _ in range(n-1):
    l.append(list(map(int,input().split())))
while True:
    cnt = 1
    for i in range(n-1):
        a,b,c,d = l[i]
        if res[a]*d==res[b]*c:
            cnt += 1
            continue
        if res[a]*d>res[b]*c:
            mul(res,a,b,c,d)
        else:
            mul(res,b,a,d,c)
    if cnt==n:
        break
t = gcd(*res)
for i in res:
    print(i//t,end=" ")