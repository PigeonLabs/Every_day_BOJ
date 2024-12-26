x = 0
n = int(input())
res = set()
l = list(map(int,input().split()))
for i in l:
    if i in res:
        x += 1
    else:
        res.add(i)
print(x)