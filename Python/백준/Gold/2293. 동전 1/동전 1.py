n,k = map(int,input().split())
l = [1]+[0]*(k)
for _ in range(n):
    t = int(input())
    for i in range(1,k+1):
        if i>=t:
            l[i] = l[i] + l[i-t]
print(l[k])