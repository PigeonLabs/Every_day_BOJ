e = input()

op,res = [],[]
o = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}

for i in e:
    if i in o:
        if i == "(":
            op.append(i)
        elif i == ")":
            while op and op[-1]!="(":
                res.append(op.pop())
            op.pop()
        else:
            while op and o[op[-1]] >= o[i]:
                res.append(op.pop())
            op.append(i)
    else:
        res.append(i)

while op:
    res.append(op.pop())
print("".join(res))