n = int(input())

i = 0
while True:
    if n<i*(i+1)//2:
        break
    else:
        i += 1
print(i-1)