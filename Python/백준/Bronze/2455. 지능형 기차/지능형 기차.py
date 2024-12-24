res,mres = 0,0
for _ in range(4):
    a,b = map(int,input().split())
    res += b-a
    mres = max(res,mres)
print(mres)