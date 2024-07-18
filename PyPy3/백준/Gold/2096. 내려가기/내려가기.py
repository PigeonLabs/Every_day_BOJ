import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l[0] = [(l[0][0],l[0][0]),(l[0][1],l[0][1]),(l[0][2],l[0][2])]
    
for i in range(1,n):
    l[i][0] = (max(l[i-1][0][0],l[i-1][1][0])+l[i][0],min(l[i-1][0][1],l[i-1][1][1])+l[i][0])
    l[i][1] = (max(l[i-1][0][0],l[i-1][1][0],l[i-1][2][0])+l[i][1],min(l[i-1][0][1],l[i-1][1][1],l[i-1][2][1])+l[i][1])
    l[i][2] = (max(l[i-1][1][0],l[i-1][2][0])+l[i][2],min(l[i-1][1][1],l[i-1][2][1])+l[i][2])

mx,mn = 0,10**6
for tmx,tmn in l[-1]:
    mx = max(tmx,mx)
    mn = min(tmn,mn)
print(mx,mn)