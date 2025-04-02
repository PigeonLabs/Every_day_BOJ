#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    int *arr = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int *prefix = malloc(sizeof(int) * (n + 1));
    prefix[0] = 0;
    for (int i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + arr[i - 1];
    }
    
    long long res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (prefix[j + 1] - prefix[i] == m) {
                res++;
            }
        }
    }
    
    printf("%lld", res);
    
    free(arr);
    free(prefix);
    
    return 0;
}
