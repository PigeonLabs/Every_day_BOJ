l1,l2 = [],[]
for i in range(4):
    l1.append(int(input()))
for i in range(2):
    l2.append(int(input()))
l1.sort(reverse=True)
l2.sort(reverse=True)
print(sum(l1[:3])+l2[0])