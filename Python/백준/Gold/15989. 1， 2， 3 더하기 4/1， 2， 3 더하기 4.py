import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    x = n//3
    for i in range(x+1):
        res += (n-i*3)//2 + 1
    print(res)