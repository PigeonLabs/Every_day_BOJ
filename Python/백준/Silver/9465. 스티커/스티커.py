for _ in range(int(input())):
    n = int(input())
    l = []
    for _ in range(2):
        l.append([0,0]+list(map(int,input().split())))
    for i in range(n):
        l[0][i+2] += max(l[1][i],l[1][i+1])
        l[1][i+2] += max(l[0][i],l[0][i+1])
    print(max(l[0][n+1],l[1][n+1]))