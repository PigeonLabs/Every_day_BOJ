import sys
input = sys.stdin.readline

def solve(n,l,road):
    bump = [0] * n
    for i in range(n-1):
        if abs(road[i+1] - road[i]) > 1:
            return 0
    for i in range(n-1):
        if road[i] > road[i+1]:
            for j in range(l):
                if i+1+j >= n:
                    return 0
                if bump[i+1+j] == 1 or road[i+1] != road[i+1+j]:
                    return 0
                bump[i+1+j] = 1
    for i in range(n-1,0,-1):
        if road[i-1] < road[i]:
            for j in range(l):
                if i-1-j < 0:
                    return 0
                if bump[i-1-j] == 1 or road[i-1] != road[i-1-j]:
                    return 0
                bump[i-1-j] = 1
    return 1

n,l = map(int, input().split())
res = 0
m = list(list(map(int, input().split())) for _ in range(n))
for i in range(n):
    res += solve(n,l,m[i])
    res += solve(n,l,[m[j][i] for j in range(n)])
print(res)