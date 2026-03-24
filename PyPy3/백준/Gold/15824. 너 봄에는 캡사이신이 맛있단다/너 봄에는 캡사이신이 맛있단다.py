import sys
input = sys.stdin.readline
MOD = 1000000007

n = int(input())
arr = sorted(map(int, input().split()))

p = [1] * n
for i in range(1, n):
    p[i] = (p[i-1] * 2) % MOD

res = 0
for i in range(n):
    res += arr[i] * (p[i] - p[n-1-i])
    res %= MOD

print(res)