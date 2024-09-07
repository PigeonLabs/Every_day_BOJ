import sys
input = sys.stdin.readline

n = int(input())
l = sorted(map(int,input().split()))

res = 4*10**9
resl = []
for i in range(n):
    a = l[i]
    tl = l[:i]+l[i+1:]
    s,e = 0,n-2
    while s!=e:
        t = a+tl[s]+tl[e]
        if abs(t)<res:
            res = abs(t)
            resl = [a,tl[s],tl[e]]
        if t>0:
            e -= 1
        elif t<0:
            s += 1
        else:
            print(*sorted([a,tl[s],tl[e]]))
            exit()
        
print(*sorted(resl))