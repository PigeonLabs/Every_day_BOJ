#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    int res = 0;
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        int t;
        scanf("%d",&t);
        res += t;
    }
    printf("%d", res-n+1);
    return 0;
}