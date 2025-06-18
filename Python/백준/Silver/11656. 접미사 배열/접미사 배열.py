w = input().strip()
l = []
for i in range(len(w)):
    l.append(w[i:])
l.sort()
for i in l:
    print(i)