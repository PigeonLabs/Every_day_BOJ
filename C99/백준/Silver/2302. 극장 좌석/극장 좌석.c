#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int sol(int n) {
    int arr[41] = {0};
    arr[0] = 1;
    arr[1] = 1;
    for (int i = 2; i <= n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    return arr[n];
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    int *seat = calloc(n, sizeof(int));
    int t;
    for (int i = 0; i < m; i++) {
        scanf("%d", &t);
        seat[t - 1] = 1;
    }
    
    int r = 0;
    int res = 1;
    
    for (int i = 0; i < n; i++) {
        if (seat[i] == 0) {
            r++;
        } else {
            if (r > 0) {
                res *= sol(r);
                r = 0;
            }
        }
    }
    if (r > 0) {
        res *= sol(r);
    }
    
    printf("%d", res);
    
    free(seat);
    return 0;
}
