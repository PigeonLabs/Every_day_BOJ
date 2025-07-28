import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())):
    res.append(int(input()))
res.sort()
print(*res,sep="\n")