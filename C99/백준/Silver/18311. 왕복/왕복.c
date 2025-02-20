#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    long long n, k;
    scanf("%lld %lld", &n, &k);
    int t[n];
    long long run[2 * n + 1];
    run[0] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &t[i]);
        run[i + 1] = run[i] + t[i];
    }
    for (int i = 0; i < n; i++) {
        run[n + i + 1] = run[n + i] + t[n - 1 - i];
    }
    for (int i = 0; i < 2 * n + 1; i++) {
        if (k < run[i]) {
            if (i <= n) {
                printf("%d", i);
            }
            else {
                printf("%d", 2 * n - i + 1);
            }
            break;
        }
    }
    
    return 0;
}
