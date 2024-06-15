import sys
input = sys.stdin.readline

l = []
n = int(input())
for _ in range(n):
    l.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            l[i][j] += l[i-1][j]
        elif j==i:
            l[i][j] += l[i-1][j-1]
        else:
            l[i][j] += max(l[i-1][j-1],l[i-1][j])
print(max(l[n-1]))