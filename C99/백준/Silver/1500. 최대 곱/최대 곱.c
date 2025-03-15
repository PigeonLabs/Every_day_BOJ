#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int s,k;
    scanf("%d %d",&s,&k);
    int l = s/k;
    int* arr = malloc(sizeof(int)*(k));
    int lo = s - k*(s/k);
    for(int i=0;i<k;i++) {
        arr[i] = s/k;
        if (lo) {
            lo--;
            arr[i]++;
        }
    }
    long long res = 1;
    for(int i=0;i<k;i++) {
        res *= arr[i];
    }
    printf("%lld",res);
    free(arr);
    return 0;
}