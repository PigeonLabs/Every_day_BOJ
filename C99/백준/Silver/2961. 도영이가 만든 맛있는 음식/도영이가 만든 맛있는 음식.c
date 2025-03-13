#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int binseq(int n,int a[], int b[]) {
    int mn = 1000000000;
    int limit = 1 << n;
    for (int i = 1; i < limit; i++) {
        int res_a = 1, res_b = 0;
        for (int x = n - 1; x >= 0; x--) {
            if ((i >> x) & 1) {
                res_a *= a[x];
                res_b += b[x];
            }
        }
        int res = res_a >= res_b ? res_a - res_b : res_b - res_a;
        mn = mn > res ? res : mn;
    }
    return mn;
}

int main(void) {
    int n;
    int a[10];
    int b[10];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a[i], &b[i]);
    }
    printf("%d",binseq(n, a, b));
    return 0;
}
