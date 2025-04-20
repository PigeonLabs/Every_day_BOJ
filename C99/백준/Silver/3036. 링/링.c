#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    }
}

int main(void) {
    int n,m,t,x;
    scanf("%d", &n);
    scanf("%d", &m);
    for (int i = 0;i < n-1;i++) {
        scanf("%d", &t);
        x = gcd(m, t);
        printf("%d/%d\n", m / x, t / x);
    }
    return 0;
}
