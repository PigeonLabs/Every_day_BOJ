#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n = 0;
    int res = 0;
    int mn = 999;
    for (int i=0;i<7;i++) {
        scanf("%d",&n);
        if (n%2) {
            res += n;
            if (n<mn) {
                mn = n;
            }
        }
    }
    if (res==0) {
        printf("-1");
    }
    else {
        printf("%d\n",res);
        printf("%d\n",mn);
    }
    return 0;
}