L = int(input())
arr = [0 for _ in range(L + 1)]
N = int(input())

pred_i = 0
pred_cnt = 0

for i in range(1, N + 1):
    P, K = map(int, input().split())
    
    current_pred_cnt = K - P + 1
    if pred_cnt < current_pred_cnt:
        pred_cnt = current_pred_cnt
        pred_i = i
        
    for j in range(P, K + 1):
        if arr[j] == 0:
            arr[j] = i

mx_cnt = 0
mx_i = 0

for i in range(1, N + 1):
    cnt = arr.count(i)
    if mx_cnt < cnt:
        mx_cnt = cnt
        mx_i = i

print(pred_i)
print(mx_i)