#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    int a,b;
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%d %d",&a,&b);
        if (a<b) {
            printf("NO BRAINS\n");
        }
        else {
            printf("MMM BRAINS\n");
        }
    }
    return 0;
}