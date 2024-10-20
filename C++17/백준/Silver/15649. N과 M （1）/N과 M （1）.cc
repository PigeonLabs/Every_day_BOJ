#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int chk(int arr[], int m) {
    for (int i=1;i<=m;i++) {
        for (int j=1;j<i;j++) {
            if (arr[i]==arr[j]) {
                return 0;
            }
        }
    }
    return 1;
}

int main(void) {
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    int arr[8] = {0};
    for (int i=1;i<=m;i++) {
        arr[i] = i;
    }
    while (arr[0]==0) {
        if (chk(arr,m)) {
            for (int i=1;i<=m;i++) {
                printf("%d ",arr[i]);
            }
            printf("\n");
        }
        arr[m]++;
        for (int i=m;i>0;i--) {
            if (arr[i]>n) {
                arr[i] = 1;
                arr[i-1]++;
            }
        }
    }
    return 0;
}