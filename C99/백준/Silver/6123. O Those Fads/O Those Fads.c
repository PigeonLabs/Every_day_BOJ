#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int int_a = *(const int *)a;
    int int_b = *(const int *)b;
    return int_a - int_b;
}

int main(void) {
    int n,l,k;
    scanf("%d %d %d",&n,&l,&k);
    int* arr = malloc(sizeof(int)*n);
    for(int i=0;i<n;i++) {
        int t;
        scanf("%d",&t);
        arr[i] = t;
    }
    qsort(arr, n, sizeof(int), compare);
    int res = 0;
    for(int i=0;i<n;i++) {
        if (arr[i]<=l) {
            res++;
            l += k;
        }
        else {
            break;
        }
    }
    printf("%d",res);
    free(arr);
    return 0;
}