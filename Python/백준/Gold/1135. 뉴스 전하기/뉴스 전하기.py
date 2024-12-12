def call(c,n):
    if len(c[n])==0:
        return 0
    t = []
    for i in c[n]:
        t.append(call(c,i))
    t.sort(reverse=True)
    for i in range(len(t)):
        t[i] += i + 1
    return max(t)

n = int(input())
p = list(map(int,input().split()))
c = []
for i in range(n):
    c.append([x for x, v in enumerate(p) if v == i])
print(call(c,0))