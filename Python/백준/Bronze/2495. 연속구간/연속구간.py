for i in range(3):
    n = input()
    res = 1
    mx = 1
    for k in range(7):
        if n[k]==n[k+1]:
            res += 1
            mx = max(mx,res)
        else:
            res = 1
    print(mx)