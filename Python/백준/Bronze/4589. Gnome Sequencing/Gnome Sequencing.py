print("Gnomes:")
for i in range(int(input())):
    l = list(map(int,input().split()))
    if l[0]>l[1]>l[2] or l[0]<l[1]<l[2]:
        print("Ordered")
    else:
        print("Unordered")