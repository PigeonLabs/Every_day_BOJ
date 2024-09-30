#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int t = n/5;
    if (n==1 || n==3) {
        printf("-1");
    }
    else if ((n % 5) % 2 == 1) {
        printf("%d",t-1+(n%5+5)/2);
    }
    else {
        printf("%d",t+(n%5)/2);
    }
    return 0;
}