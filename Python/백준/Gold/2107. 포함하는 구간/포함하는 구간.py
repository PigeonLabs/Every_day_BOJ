import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort()
res = 0
for i in range(n-1):
    c = 0
    for j in range(i+1,n):
        if l[j][1]<l[i][1]:
            c += 1
        elif l[i][1]<l[j][0]:
            break
    res = max(res,c)

print(res)