while True:
    n = input()
    if (n=='0'):
        break
    t = 0
    while n!=n[::-1]:
        n = str(int(n)+1).zfill(len(n))
        t += 1
    print(t)