n = int(input())
l = list(map(int,input().split()))
t = []

res = [1]*n
 
for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            res[i] = max(res[i], res[j]+1)
 
print(max(res))