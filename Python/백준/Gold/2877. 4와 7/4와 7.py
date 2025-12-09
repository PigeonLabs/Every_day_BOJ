n = int(input())-1
t = 1
while True:
    if n < 2**t:
        break
    n -= 2**t
    t += 1
s = bin(n)[2:].zfill(t).replace('0', '4').replace('1', '7')
print(s)