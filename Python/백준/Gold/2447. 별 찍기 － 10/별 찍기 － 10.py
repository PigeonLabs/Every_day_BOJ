n = int(input())

arr = [['*']*n for _ in range(n)]

x = 3
while x <= n:
    for i in range(0,n,x):
        for j in range(0,n,x):
            for k in range(x//3):
                for l in range(x//3):
                    arr[i+k+x//3][j+l+x//3] = ' '
    x *= 3

for row in arr:
    print(''.join(row))