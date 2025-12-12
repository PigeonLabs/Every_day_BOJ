import sys
input = sys.stdin.readline

def wd(s):
    for i in range(len(s)-1):
        res = set()
        for x in range(len(s)-1-i):
            if s[x]+s[x+i+1] not in res:
                res.add(s[x]+s[x+i+1])
            else:
                return False
    return True

while (s:=input().strip())!='*':
    print(s,end=' ')
    if wd(s):
        print("is surprising.")
    else:
        print("is NOT surprising.")