def sch(l,n):
    mx = 0
    for i in range(n-2,n+3):
        c = 0
        for x in range(i-2,i+3):
            if x>=0:
                if x in l:
                    c += 1
        mx = max(mx,c)
    return mx

n = int(input())
l = set()
for _ in range(n):
    l.add(int(input()))
m = 0
for t in l:
    m = max(m,sch(l,t))
print(5-m)