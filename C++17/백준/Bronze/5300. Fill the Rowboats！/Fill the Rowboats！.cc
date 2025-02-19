#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d",&n);
    for(int i=1;i<n+1;i++) {
        printf("%d ",i);
        if (i%6==0) {
            printf("Go! ");
        }
    }
    if (n%6!=0) {
        printf("Go!");
    }
    return 0;
}