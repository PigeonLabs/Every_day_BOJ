n = int(input())
g = sorted(list(map(int,input().split())))
l,r = 0,n-1
res = []
res.append((abs(g[l]+g[r]),l,r))
while r-l!=1:
    if abs(g[l+1]+g[r])<abs(g[l]+g[r-1]):
        l += 1
    else:
        r -= 1
    res.append((abs(g[l]+g[r]),l,r))
res.sort()
print(g[res[0][1]],g[res[0][2]])