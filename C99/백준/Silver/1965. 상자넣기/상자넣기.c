#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d",&n);
    int *arr = malloc(sizeof(int)*n);
    for(int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
    }
    int *d = malloc(sizeof(int)*n);
    d[0] = arr[0];
    int cnt = 1;
    for(int i=1;i<n;i++) {
        if (d[cnt-1]<arr[i]) {
            d[cnt++] = arr[i];
        }
        else {
            int j = 0;
            while (j < cnt && d[j] < arr[i]) {
                j++;
            }
            d[j] = arr[i];
        }
    }
    printf("%d",cnt);
    free(arr);
    free(d);
    return 0;
}
