import sys
input = sys.stdin.readline

num = [0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
    
while True:
    try:
        line = list(input().strip())
        res = [0]
        if not line:
            break
        for x in line:
            if num[ord(x)-65] != res[-1]:
                res.append(num[ord(x)-65])
        for r in res[1:]:
            if r:
                print(r, end="")
        print()
    except:
        break