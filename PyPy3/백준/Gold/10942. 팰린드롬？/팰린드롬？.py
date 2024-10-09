import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
x = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    x[i][i] = 1

for i in range(n - 1):
    if l[i] == l[i + 1]:
        x[i][i + 1] = 1

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if l[i] == l[j] and x[i + 1][j - 1] == 1:
            x[i][j] = 1

m = int(input())
for i in range(m):
    s,e = map(int,input().split())
    print(x[s-1][e-1])