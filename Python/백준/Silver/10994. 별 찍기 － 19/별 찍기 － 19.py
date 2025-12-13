n = int(input())
h = 4*n-3
arr = [[" "] * (h) for _ in range(h)]
for i in range(0,h//2,2):
    for o in range(i,h-i):
        arr[i][o] = "*"
        arr[o][i] = "*"
        arr[h-1-i][o] = "*"
        arr[o][h-1-i] = "*"
arr[h//2][h//2] = "*"
for row in arr:
    print("".join(row))