c = 0
for n in range(1,int(input())+1):
    n = list(map(int,list(str(n))))
    s = set()
    for i in range(len(n)-1):
        s.add(n[i]-n[i+1])
    if len(s)<=1:
        c += 1
print(c)