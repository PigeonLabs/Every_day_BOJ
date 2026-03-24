import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        res += pow(2, j-i-1, 1000000007) * (arr[j]-arr[i]) % 1000000007
    res %= 1000000007
print(res)