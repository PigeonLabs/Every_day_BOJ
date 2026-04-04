import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * 100001
for i in range(n):
    num = int(input())
    arr[num] = i+1

ans = 0
for i in range(1, n):
    if arr[i]>arr[i+1]:
        ans += 1

print(ans)