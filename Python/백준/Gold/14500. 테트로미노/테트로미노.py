N,M=map(int,input().split())
m=[]
for _ in range(N):
    m.append(list(map(int,input().split())))
a=0

#1
for i in range(N):
    for j in range(M-3):
        n=m[i][j]+m[i][j+1]+m[i][j+2]+m[i][j+3]
        if a<n:
            a=n

#2
for i in range(N-3):
    for j in range(M):
        n=m[i][j]+m[i+1][j]+m[i+2][j]+m[i+3][j]
        if a<n:
            a=n

#3
for i in range(N-1):
    for j in range(M-1):
        n=m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1]
        if a<n:
            a=n

#4
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j]+m[i+1][j]+m[i+2][j]+m[i+2][j+1]
        if a<n:
            a=n

#5
for i in range(N-1):
    for j in range(M-2):
        n=m[i+1][j]+m[i+1][j+1]+m[i+1][j+2]+m[i][j+2]
        if a<n:
            a=n

#6
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j]+m[i][j+1]+m[i+1][j+1]+m[i+2][j+1]
        if a<n:
            a=n

#7
for i in range(N-1):
    for j in range(M-2):
        n=m[i][j]+m[i+1][j]+m[i][j+1]+m[i][j+2]
        if a<n:
            a=n

#8
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j]+m[i+1][j]+m[i+1][j+1]+m[i+2][j+1]
        if a<n:
            a=n

#9
for i in range(N-1):
    for j in range(M-2):
        n=m[i+1][j]+m[i+1][j+1]+m[i][j+1]+m[i][j+2]
        if a<n:
            a=n

#10
for i in range(N-1):
    for j in range(M-2):
        n=m[i][j]+m[i][j+1]+m[i+1][j+1]+m[i+1][j+2]
        if a<n:
            a=n

#11
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j+1]+m[i+1][j+1]+m[i+1][j]+m[i+2][j]
        if a<n:
            a=n

#12
for i in range(N-2):
    for j in range(M-1):
        n=m[i+2][j]+m[i+2][j+1]+m[i+1][j+1]+m[i][j+1]
        if a<n:
            a=n

#13
for i in range(N-1):
    for j in range(M-2):
        n=m[i][j]+m[i+1][j]+m[i+1][j+1]+m[i+1][j+2]
        if a<n:
            a=n

#14
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j+1]+m[i][j]+m[i+1][j]+m[i+2][j]
        if a<n:
            a=n

#15
for i in range(N-1):
    for j in range(M-2):
        n=m[i][j]+m[i][j+1]+m[i][j+2]+m[i+1][j+2]
        if a<n:
            a=n

#16
for i in range(N-1):
    for j in range(M-2):
        n=m[i+1][j]+m[i+1][j+1]+m[i][j+1]+m[i+1][j+2]
        if a<n:
            a=n

#17
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j+1]+m[i+1][j]+m[i+1][j+1]+m[i+2][j+1]
        if a<n:
            a=n

#18
for i in range(N-1):
    for j in range(M-2):
        n=m[i][j]+m[i][j+1]+m[i][j+2]+m[i+1][j+1]
        if a<n:
            a=n

#19
for i in range(N-2):
    for j in range(M-1):
        n=m[i][j]+m[i+1][j]+m[i+1][j+1]+m[i+2][j]
        if a<n:
            a=n

print(a)