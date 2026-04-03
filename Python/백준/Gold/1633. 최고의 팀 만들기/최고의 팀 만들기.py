import sys

ab = []
for line in sys.stdin:
    ab.append(tuple(map(int, line.split())))

INF = -10**8
n = len(ab)

arr = [[[INF] * 16 for _ in range(16)] for _ in range(n+1)]
arr[0][0][0] = 0

for i in range(1, n+1):
    a, b = ab[i-1]
    for j in range(16):
        for k in range(16):
            arr[i][j][k] = arr[i-1][j][k]
            if j > 0:
                arr[i][j][k] = max(arr[i][j][k], arr[i-1][j-1][k] + a)
            if k > 0:
                arr[i][j][k] = max(arr[i][j][k], arr[i-1][j][k-1] + b)

print(arr[n][15][15])