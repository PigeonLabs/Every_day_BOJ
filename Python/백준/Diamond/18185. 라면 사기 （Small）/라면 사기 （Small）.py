import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s1 = s2 = res = 0

for x in arr:
    new_s2 = min(x, s1)
    x -= new_s2
    new_s3 = min(x, s2)
    x -= new_s3
    res += (new_s2 + new_s3) * 2 + x * 3
    s1, s2 = x, new_s2

print(res)