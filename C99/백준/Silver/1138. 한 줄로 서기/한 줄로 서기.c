#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    int arr[10];
    int res[10] = {0};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        int t=arr[i];
        int idx=0;
        while(1) {
            if (res[idx] == 0) {
                if (t == 0) break;
                t--;
                }
            idx++;
        }
        res[idx] = i+1;
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", res[i]);
    }
    return 0;
}