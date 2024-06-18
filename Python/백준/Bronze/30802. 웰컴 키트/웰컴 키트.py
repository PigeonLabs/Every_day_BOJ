n = int(input())
l = list(map(int,input().split()))
t,p = map(int,input().split())
s = 0
for i in l:
    if i-1>=0:
        s += ((i-1)//t)+1
print(s)
print(n//p,n%p)