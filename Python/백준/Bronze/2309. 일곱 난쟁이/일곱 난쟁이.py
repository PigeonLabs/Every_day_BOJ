arr = []
for _ in range(9):
    f=int(input())
    arr.append(f)
arr.sort()


sum_ = sum(arr)
fake=[]
for i in range(9):
    for j in range(i+1,9):
        if(len(fake)==2):
            continue
        if sum_-arr[i]-arr[j] ==100:
            fake.append(arr[i])
            fake.append(arr[j])

for i in arr:
    if i in fake:
        continue
    print(i)