import sys
input = sys.stdin.readline
while True:
    nx,ny,w = map(float,input().split())
    nx = int(nx)
    ny = int(ny)
    if nx==0 and ny==0 and w==0:
        exit()
    xi = sorted(list(map(float,input().split())))
    yi = sorted(list(map(float,input().split())))
    res = 1
    if xi[0]-w/2>0 or xi[-1]+w/2<75 or yi[0]-w/2>0 or yi[-1]+w/2<100:
        res = 0
    else:
        for i in range(nx-1):
            if xi[i+1]-xi[i]>w:
                res = 0
                break;
        if res:
            for i in range(ny-1):
                if yi[i+1]-yi[i]>w:
                    res = 0
                    break;
    if res:
        print("YES")
    else:
        print("NO")