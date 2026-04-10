import sys
input = sys.stdin.readline

def solve(arr, m):
    lines = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
    ]
    for line in lines:
        res = 0
        cnt = False
        y,x = 0,0
        for i, j in line:
            if arr[i][j] == m:
                res += 1
            if arr[i][j] == '-':
                y = i
                x = j
                cnt = True
        if cnt and res == 2:
            arr[y][x] = m
            return True
    return False

t = int(input())
for i in range(t):
    arr = [list(input().strip()) for _ in range(3)]
    m = input().strip()
    print(f'Case {i+1}:')
    if solve(arr, m):
        for row in arr:
            print(''.join(row))