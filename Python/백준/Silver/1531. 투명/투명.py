import sys
input = sys.stdin.readline

l = [[0 for _ in range(101)] for _ in range(101)]
res = 0

n,m = map(int,input().split())
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            l[i][j] += 1
            if l[i][j] == m+1:
                res += 1
                
print(res)