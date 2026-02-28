n,k = map(int,input().split())
s = input().strip()
q = []
left = k
for num in s:
    while left and q and q[-1] < num:
        q.pop()
        left -= 1
    q.append(num)
print(*q[:n-k],sep='')