import sys
input = sys.stdin.readline

def solve(s,e):
    if s == e:
        return t[s]
    mid = (s+e)//2
    l,r = mid,mid+1
    minh = min(t[l],t[r])
    ans = minh * 2
    while l > s or r < e:
        if l == s:
            r += 1
            minh = min(minh, t[r])
        elif r == e:
            l -= 1
            minh = min(minh, t[l])
        elif t[l - 1] < t[r + 1]:
            r += 1
            minh = min(minh, t[r])
        else:
            l -= 1
            minh = min(minh, t[l])
        ans = max(ans, minh * (r - l + 1))
    return max(ans, solve(s,mid), solve(mid+1,e))

n = int(input())
t = list(map(int,input().split()))
print(solve(0,n-1))