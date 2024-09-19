#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n,t;
    int r = 0;
    scanf("%d",&n);
    int arr[51] = {0};
    for (int i=0;i<n;i++) {
        scanf("%d",&t);
        arr[t]++;
    }
    for (int i = 50; i >= 0; i--) {
        if (arr[i]==i) {
            printf("%d",i);
            r = 1;
            break;
        }
    }
    if (r == 0) {
        printf("-1");
    }
    return 0;
}