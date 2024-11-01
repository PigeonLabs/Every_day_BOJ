import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = list(map(int,input().split()))
lm = []
lp = []
mx = 0
for i in l:
    if i<0:
        lm.append(i)
        if mx<-i:
            mx = -i
    else:
        lp.append(i)
        if mx<i:
            mx = i
lm.sort()
lp.sort(reverse=True)

res = -mx
for i in range(0,len(lm),m):
    res -= lm[i]*2
for i in range(0,len(lp),m):
    res += lp[i]*2

print(res)