n, r, c = map(int,input().split())

def quadrant(n,r,c):
    if n==0:
        return 0
    ct = 2**(n-1)
    if r<ct and c<ct:
        return quadrant(n-1,r,c)
    elif r<ct and c>=ct:
        return (4**(n-1))+quadrant(n-1,r,c-ct)
    elif r>=ct and c<ct:
        return 2*(4**(n-1))+quadrant(n-1,r-ct,c)
    else:
        return 3*(4**(n-1))+quadrant(n-1,r-ct,c-ct)
        
print(quadrant(n,r,c))