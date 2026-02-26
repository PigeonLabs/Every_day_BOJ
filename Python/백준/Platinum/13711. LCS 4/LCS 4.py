import sys,bisect
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pos = [0 for _ in range(n)]
T = []
for i in range(n):
    pos[A[i]-1] = i
for i in range(n):
    T.append(pos[B[i]-1])

LIS = [T[0]]
for x in T:
    if LIS[-1] < x:
        LIS.append(x)
    else:
        LIS[bisect.bisect_left(LIS,x)] = x

print(len(LIS))