a = int(input())
l = list(map(int,input().split()))
lr = l[::-1]
res,resr = [1],[1]
rest,resrt = [l[0]],[lr[0]]
restl,resrtl = 1,1

for i in range(a-1):
    if l[i+1]>rest[-1]:
        res.append(restl+1)
        rest.append(l[i+1])
        restl += 1
    else:
        t = 0
        while rest[t]<l[i+1]:
            t += 1
        rest[t] = l[i+1]
        res.append(t+1)
    
    if lr[i+1]>resrt[-1]:
        resr.append(resrtl+1)
        resrt.append(lr[i+1])
        resrtl += 1
    else:
        t = 0
        while resrt[t]<lr[i+1]:
            t += 1
        resrt[t] = lr[i+1]
        resr.append(t+1)

r = 0
for i in range(a):
    r = max(r,res[i]+resr[-i-1])

print(r-1)