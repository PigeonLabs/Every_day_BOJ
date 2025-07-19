import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
res = [1]
for i in range(1,n):
        res.insert(i-l[i],i+1)
print(*res)