import sys
input = sys.stdin.readline

n = int(input())
l = []
mx = 0
for i in range(n):
    a,b = map(int,input().split())
    mx = max(mx,b)
    l.append((b,a))
l.sort(reverse=True)
for b,a in l:
    mx = min(mx,b)-a
if mx>=0:
    print(mx)
else:
    print(-1)