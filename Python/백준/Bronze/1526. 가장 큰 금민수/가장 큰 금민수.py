N = int(input())
for number in range(N,1,-1):
    word = str(number)
    cnt = 0
    for w in word :
        if w == '7' :
            cnt += 1
        elif w == '4' :
            cnt += 1
    if cnt == len(word) :
        print(number)
        break
    else :
        continue