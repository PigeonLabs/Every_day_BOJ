import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(map(str, input().split()))
    x = (arr[4], arr[5], arr[6], arr[7])
    o = {
    (arr[0], arr[1], arr[2], arr[3]),
    (arr[0], arr[2], arr[3], arr[1]),
    (arr[0], arr[3], arr[1], arr[2]),
    (arr[1], arr[0], arr[3], arr[2]),
    (arr[1], arr[3], arr[2], arr[0]),
    (arr[1], arr[2], arr[0], arr[3]),
    (arr[2], arr[0], arr[1], arr[3]),
    (arr[2], arr[1], arr[3], arr[0]),
    (arr[2], arr[3], arr[0], arr[1]),
    (arr[3], arr[0], arr[2], arr[1]),
    (arr[3], arr[2], arr[1], arr[0]),
    (arr[3], arr[1], arr[0], arr[2]),
    }
    
    print(1 if x in o else 0)