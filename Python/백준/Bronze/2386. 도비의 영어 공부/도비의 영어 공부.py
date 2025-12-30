while True:
    S = list(map(str, input().split()))
    find = S[0]
    target = S[1:]
    if find == '#':
        break
    print(find, str(target).lower().count(find))