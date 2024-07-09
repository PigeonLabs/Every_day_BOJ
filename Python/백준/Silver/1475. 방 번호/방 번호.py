l = [0]*10
for i in list(input()):
    i = int(i)
    l[i] += 1
print(max((l.pop(6)+l.pop(8)+1)//2,max(l)))