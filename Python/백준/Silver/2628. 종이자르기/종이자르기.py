x,y = list(map(int, input().split()))
xcut,ycut = [0,x],[0,y]
for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    if a:
        xcut.append(b)
    else:
        ycut.append(b)
xcut.sort()
ycut.sort()
xres,yres,res = [],[],[]
for i in range(len(xcut)-1):
    xres.append(xcut[i+1]-xcut[i])
for i in range(len(ycut)-1):
    yres.append(ycut[i+1]-ycut[i])
for i in xres:
    for j in yres:
        res.append(i*j)
print(max(res))