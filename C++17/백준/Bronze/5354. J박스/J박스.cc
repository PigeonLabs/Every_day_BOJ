#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        int t;
        scanf("%d",&t);
        if (t==1) {
            printf("#");
            if (i!=n-1) {
                printf("\n");
            } 
        }
        else {
            for(int x=0;x<t;x++) {
                printf("#");
            }
            printf("\n");
            for(int i=0;i<t-2;i++) {
                printf("#");
                for(int v=0;v<t-2;v++) {
                    printf("J");
                }
                printf("#\n");
            }
            for(int x=0;x<t;x++) {
                printf("#");
            }
            printf("\n");
        }
        if (i!=n-1) {
            printf("\n");
        }
    }
    return 0;
}