n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
print(sum([max(l[i] - i, 0) for i in range(len(l))]))