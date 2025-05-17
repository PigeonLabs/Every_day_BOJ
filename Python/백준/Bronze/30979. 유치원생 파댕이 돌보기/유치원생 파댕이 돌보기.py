t = int(input())
n = int(input())
l = list(map(int, input().split()))

if t <= sum(l):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")