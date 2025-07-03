n = int(input())
l = list(map(int, input().split()))
m1 = min(l)
m2 = min(l[0]+l[1],l[0]+l[2],l[0]+l[3],l[0]+l[4],
         l[5]+l[1],l[5]+l[2],l[5]+l[3],l[5]+l[4],
         l[1]+l[2],l[1]+l[3],l[4]+l[2],l[4]+l[3],)
m3 = min(l[0]+l[1]+l[2],l[0]+l[1]+l[3],
         l[0]+l[4]+l[2],l[0]+l[4]+l[3],
         l[5]+l[1]+l[2],l[5]+l[1]+l[3],
         l[5]+l[4]+l[2],l[5]+l[4]+l[3],)
if n==1:
    print(sum(l)-max(l))
else:
    print(m3*4+m2*(2*n-3)*4+m1*(5*(n-2)**2+4*(n-2)))