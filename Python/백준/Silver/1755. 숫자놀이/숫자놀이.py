num_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

m,n = map(int, input().split())
l = []
for i in range(m,n+1):
    temp = []
    for x in list(str(i)):
        temp.append(num_dict[x])
    l.append([" ".join(temp),i])
l.sort()
for i in range(len(l)):
    print(l[i][1],end=" ")
    if (i+1)%10==0:
        print("")