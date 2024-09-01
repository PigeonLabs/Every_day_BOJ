n = list(map(int,input().split()))
res = 0
for s in range(2):
    for i in range(54):
        t = 2**i
        r = 2**(i+1)
        if s:
            res += ((n[s]+t)//r)*t
            if t<=n[s]%r<r-1:
                res -= (r-1)-n[s]%r
        else:
            res -= (((n[s]-1)+t)//r)*t
            if t<=(n[s]-1)%r<r-1:
                res += (r-1)-(n[s]-1)%r

print(res)