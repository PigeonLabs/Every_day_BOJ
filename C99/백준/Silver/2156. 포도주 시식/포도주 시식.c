#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define max(x, y) ((x) > (y) ? (x) : (y))

void solve(int n, int* arr, int* res) {
    res[0] = arr[0];
    res[1] = arr[0]+arr[1];
    res[2] = max(arr[0] + arr[2], max(arr[1] + arr[2], arr[0] + arr[1]));
    for (int i=3;i<n;i++) {
        int c1 = res[i-1];
        int c2 = res[i-2] + arr[i];
        int c3 = res[i-3] + arr[i-1] + arr[i];
        res[i] = max(c1,max(c2,c3));
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int* arr = malloc(sizeof(int)*n);
    int* res = calloc(n,sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    if (n==1) {
        printf("%d",arr[0]);
    }
    else if (n==2) {
        printf("%d",arr[0]+arr[1]);
    }
    else {
        solve(n,arr,res);
        printf("%d",res[n-1]);
    }
    free(arr);
    free(res);
    return 0;
}