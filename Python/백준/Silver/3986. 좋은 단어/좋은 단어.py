import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for _ in range(n):
    l = input().strip()
    res = []
    for x in l:
        if (len(res)==0) or res[-1]!=x:
            res.append(x)
        else:
            res.pop()
    if len(res)==0:
        ans += 1

print(ans)