#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int f;
    scanf("%d", &f);
    int p = f;
    int res = 0;
    int t;
    for (int i = 0; i < n - 1; i++) {
        scanf("%d", &t);
        if (t <= p) {
            res++;
        }
        p = t;
    }
    if (f <= t) {
        res++;
    }
    printf("%d", res);
}