n = int(input())
c = 0
while n>9:
    n = sum(int(i) for i in str(n))
    c += 1
print(c)
print("YES" if n%3==0 else "NO")