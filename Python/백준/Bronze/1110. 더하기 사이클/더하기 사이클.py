n = int(input())
t = n
c = 1

while True:
    t = t%10*10+sum(map(int,list(str(t))))%10
    if n==t:
        print(c)
        exit()
    c += 1