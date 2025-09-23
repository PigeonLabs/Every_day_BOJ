while True:
    member = list(map(str,input().split()))
    if int(member[1])==0 and int(member[2])==0:
        break
    print(member[0],end=" ")
    if 17<int(member[1]) or 80<=int(member[2]):
        print("Senior")
    else:
        print("Junior")