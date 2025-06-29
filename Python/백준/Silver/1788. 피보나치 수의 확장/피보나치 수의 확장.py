a,b = 0,1
n = int(input())
if n==0:
    print(0)
    print(0)
    exit()
for i in range(abs(n)-1):
    a,b = b,(a+b)%10**9
if n<0 and abs(n)%2==0:
    print(-1)
else:
    print(1)
print(b)