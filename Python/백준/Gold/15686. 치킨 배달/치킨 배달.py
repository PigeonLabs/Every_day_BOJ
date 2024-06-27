from itertools import combinations

n,m = map(int,input().split())
l = []
dst = []
home_index = []
chicken_index = []
for i in range(n):
    l.append(list(map(int,input().split())))
    for j in list(filter(lambda x: l[i][x] == 1, range(n))):
        home_index.append((i,j))
    for j in list(filter(lambda x: l[i][x] == 2, range(n))):
        chicken_index.append((i,j))
for ci,ck in chicken_index:
    dst.append([abs(ci-hi)+abs(ck-hk) for hi,hk in home_index])
res = 1e8
for i in list(combinations(dst,m)):
    minval = 0
    for j in zip(*i):
        minval += min(j)
    res = min(res,minval)
print(res)