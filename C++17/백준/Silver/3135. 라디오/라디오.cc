#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a,b,n;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&n);
    int mn = abs(a-b);
    for (int i=0;i<n;i++) {
        int f;
        scanf("%d",&f);
        if (abs(f-b)+1<mn) {
            mn = abs(f-b)+1;
        }
    }
    printf("%d",mn);

    return 0;
}