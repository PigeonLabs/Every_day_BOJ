import sys
input = sys.stdin.readline

a = input().strip()
cnt = 1

for i in range(len(a)-1):
    if  ord(a[i]) >= ord(a[i+1]):
        cnt += 1

print(cnt)