#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int x=1, res=0;
    while (x<n) x*=2;
    printf("%d ", x);
    while (n) {
        if (x<=n) n-=x;
        x/=2;
        if (n==0) break;
        res++;
    }
    printf("%d\n", res);
    return 0;
}