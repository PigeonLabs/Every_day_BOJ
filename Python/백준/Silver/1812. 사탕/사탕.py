import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
v = 0
for idx,val in enumerate(l):
    if idx&1==0:
        v += val
    else:
        v -= val
res = [v//2]
for i in range(n-1):
    res.append(l[i]-res[i])
for i in res:
    print(i)