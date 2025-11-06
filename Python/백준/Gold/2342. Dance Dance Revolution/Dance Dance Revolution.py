import sys
input = sys.stdin.readline

l = list(map(int, input().split()))

step = [[[10**8 for _ in range(5)] for _ in range(5)] for _ in range(len(l))]
step[0][0][0] = 0

def sol(a,b):
    if a==0:
        return 2
    elif a==b:
        return 1
    elif abs(a-b)==2:
        return 4
    else:
        return 3

for i in range(len(l)-1):
    for left in range(5):
        for right in range(5):
            step[i+1][left][l[i]] = min(step[i+1][left][l[i]], step[i][left][right]+sol(right,l[i]))
            step[i+1][l[i]][right] = min(step[i+1][l[i]][right], step[i][left][right]+sol(left,l[i]))
print(min(map(min, step[len(l)-1])))