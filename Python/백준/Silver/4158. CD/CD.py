import sys
input = sys.stdin.readline

while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    arr = []
    for _ in range(a):
        arr.append(int(input()))
    i,res = 0,0
    for _ in range(b):
        t = int(input())
        while i<a-1 and arr[i]<t:
            i += 1
        if arr[i]==t:
            res += 1
    print(res)