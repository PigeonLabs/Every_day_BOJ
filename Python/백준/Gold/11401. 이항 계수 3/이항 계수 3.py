import sys
input = sys.stdin.readline

MOD = 1000000007

n, k = map(int, input().split())
k = min(k, n - k)

up = 1
down = 1

for i in range(1, k + 1):
    up = up * (n - k + i) % MOD
    down = down * i % MOD

print(up * pow(down, MOD - 2, MOD) % MOD)