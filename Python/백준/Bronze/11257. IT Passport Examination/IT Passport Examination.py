import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x,a,b,c = map(int, input().split())
    print(x,a+b+c,end=" ")
    if a>=10.5 and b>=7.5 and c>=12 and a+b+c>=55:
        print("PASS")
    else:
        print("FAIL")