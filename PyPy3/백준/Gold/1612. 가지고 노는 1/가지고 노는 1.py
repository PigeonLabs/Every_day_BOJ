n = int(input())
t = l = 1

if n%10 in {0,2,4,5,6,8}:
    print(-1)
    exit()

while t%n!=0:
    t = (t%n)*10+1
    l += 1
print(l)