import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
c = max(l)
while True:
    b = False
    res = l[0]%c
    for i in l[1:]:
        if res != i%c:
            b = True
            break
    if b == True:
        c -= 1
    else:
        print(c)
        exit()