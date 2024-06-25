n,m = map(int,input().split())
t = list(map(int,input().split()))
if t[0]==0:
    for i in range(m):
        input()
    print(m)
else:
    l = []
    truth = set(t[1:])
    for i in range(m):
        l.append(set(list(map(int,input().split()))[1:]))
    i,ic,c = 0,0,0
    while True:
        if truth&l[i]:
            new = truth|l[i]
            if truth != new:
                truth = new
                ic = 0
            else:
                ic += 1
        else:
            ic += 1
        if ic==m:
            break
        i += 1
        if i==m:
            i = 0
    for k in l:
        if not (truth&k):
            c += 1
    print(c)