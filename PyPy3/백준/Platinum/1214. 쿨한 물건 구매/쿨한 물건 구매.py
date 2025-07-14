d,p,q = map(int,input().split())
if p < q:
    p,q = q,p

mn = ((d+p-1)//p)*p
for np in range(0,min(d+1,p*q),p):
    mn = min(mn,np+(d-np+q-1)//q*q)
print(mn)