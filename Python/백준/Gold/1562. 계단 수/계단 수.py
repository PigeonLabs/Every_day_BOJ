import sys
input = sys.stdin.readline
n = int(input())
num_range = 10
bit_range = 1 << num_range
MOD = 10**9;
DP = [[[0]*(bit_range) for _ in range(num_range)] for _ in range(n+1)]

for k in range(num_range):
  DP[1][k][1<<k] = 1

for i in range(1,n):
  for j in range(num_range):
    for b in range(bit_range):
      if 0<=j<9:
        more = b | 1<<(j+1)
        DP[i+1][j+1][more] += DP[i][j][b]
        DP[i+1][j+1][more] %= MOD
      if 0<j<=9:
        less = b | 1<<(j-1)
        DP[i+1][j-1][less] += DP[i][j][b]
        DP[i+1][j-1][less] %= MOD

total = 0
for k in range(1,num_range):
  total += DP[n][k][0b1111111111]
  total%=MOD
print(total)