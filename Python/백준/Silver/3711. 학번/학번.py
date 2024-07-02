for _ in range(int(input())):
    l = set()
    n = int(input())
    for _ in range(n):
        l.add(int(input()))
    l2 = set()
    t = 1
    while len(l2)!=n:
        l2 = set()
        for i in l:
            l2.add(i%t)
        t += 1
    print(t-1)