def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_all(n):
    res = n[0]
    for i in n[1:]:
        if i:
            res = lcm(res, i)
    return res

def int_to_list(n):
    return list(map(int, str(n)))

def list_to_int(n):
    return int("".join(map(str, n)))

n = list(map(int, input().strip()))
intn = list_to_int(n)

t = lcm_all(n)

if intn % t == 0:
    print(intn)
    exit()

new_n = n.copy()
new_intn = intn
while str(new_intn - new_intn % t + t)[:len(n)] != str(intn):
    new_n.append(0)
    new_intn *= 10
    if new_intn % t == 0:
        print(new_intn)
        exit()

print(new_intn - new_intn % t + t)