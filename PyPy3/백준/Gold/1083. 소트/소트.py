import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
s = int(input())

for i in range(n):
    if s <= 0:
        break
    idx = i
    for j in range(i+1,min(n,i+1+s)):
        if l[j]>l[idx]:
            idx = j
    if idx-i>0:
        l = l[:i]+[l[idx]]+l[i:idx]+l[idx+1:]
        s -= idx-i

print(*l)