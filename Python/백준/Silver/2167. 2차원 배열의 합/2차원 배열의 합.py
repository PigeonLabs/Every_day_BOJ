import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
k = int(input())
for _ in range(k):
    res = 0
    i,j,x,y = map(int,input().split())
    for q in range(i-1,x):
        res += sum(l[q][j-1:y])
    print(res)