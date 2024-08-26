import sys
input = sys.stdin.readline

n,s = map(int,input().split())
g = [0]+list(map(int,input().split()))
for i in range(1,len(g)):
    g[i] += g[i-1]
l,r,res = 0,1,10**6
if g[0]>=s:
    print(1)
    exit()
while r<=n and l<=n:
    if g[r]-g[l]>=s:
        l += 1
        res = min(res,r-l+1)
    else:
        r += 1

print(res if res!=10**6 else 0)