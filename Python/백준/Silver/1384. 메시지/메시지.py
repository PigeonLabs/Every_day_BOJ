import sys
input = sys.stdin.readline

group = 1
while True:
    n = int(input())
    if n == 0:
        break
    if group > 1:
        print()
    names = []
    v = []
    for i in range(n):
        name, *arr = list(input().split())
        for j in range(n-1):
            if arr[j] == 'N':
                v.append((j+1,i))
        names.append(name)
    print("Group",group)
    if not v:
        print("Nobody was nasty")
    else:
        for n1, n2 in v:
            print(f"{names[n2-n1]} was nasty about {names[n2]}")
    group += 1