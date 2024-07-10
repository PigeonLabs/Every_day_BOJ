res = []
for i in range(int(input())):
    res.append(list(map(int,input().split())))
    if i>0:
        res[i][0] += min(res[i-1][1],res[i-1][2])
        res[i][1] += min(res[i-1][0],res[i-1][2])
        res[i][2] += min(res[i-1][0],res[i-1][1])
print(min(res[-1]))