import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    d = list(map(str, input().split()))
    l.append([d[0],int(d[1]),int(d[2]),int(d[3])])
l.sort(key=lambda x:(-x[3],-x[2],-x[1],x[0]))
print(l[0][0])
print(l[-1][0])