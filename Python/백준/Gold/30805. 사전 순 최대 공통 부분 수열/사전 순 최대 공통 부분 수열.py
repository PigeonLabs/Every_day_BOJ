a = int(input())
la = list(map(int,input().split()))
b = int(input())
lb = list(map(int,input().split()))

res = []
cm = set(la)&set(lb)
if cm:
    fla = list(filter(lambda x: x in cm,la[la.index(max(cm)):]))
    flb = list(filter(lambda x: x in cm,lb[lb.index(max(cm)):]))
    for t in sorted(cm,reverse=True):
        ta = [i for i, value in enumerate(fla) if value == t]
        tb = [i for i, value in enumerate(flb) if value == t]
        c = min(len(ta),len(tb))
        if c>0:
            for i in range(c):
                res.append(t)
            fla = fla[ta[c-1]:]
            flb = flb[tb[c-1]:]
    print(len(res))
    print(*res)
else:
    print(0)