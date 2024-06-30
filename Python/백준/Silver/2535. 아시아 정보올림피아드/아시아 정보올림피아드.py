l = []
c = {}

for _ in range(int(input())):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x : -x[2])

res = []
i = 0
while len(res)<3:
    c[l[i][0]] = c.get(l[i][0], 0) + 1
    if c[l[i][0]]<3:
        res.append(l[i][0:2])
    i += 1

for w in res:
    print(*w)