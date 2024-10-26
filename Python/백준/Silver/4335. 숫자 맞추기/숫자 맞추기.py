import sys
input = sys.stdin.readline

res = 1
while res:
    mx,mn = 11,0
    while True:
        n = int(input())
        if n==0:
            res = 0
            break
        s = input().strip()
        if s=="too high":
            mx = min(mx,n)
        elif s=="too low":
            mn = max(mn,n)
        else:
            if mn<n<mx:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            break