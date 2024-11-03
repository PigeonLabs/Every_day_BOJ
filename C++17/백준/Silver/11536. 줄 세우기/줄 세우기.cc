# define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    int r1=0,r2=0;
    char ch[20][20];
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%s",ch[i]);
        if (i) {
            if (strcmp(ch[i-1],ch[i])<0) {
            r1++;
            }
        else if (strcmp(ch[i-1],ch[i])>0) {
            r2++;
            }
        }  
    }
    if (r1>0 && r2==0) {
        printf("INCREASING");
    }
    else if (r1==0 && r2>0) {
        printf("DECREASING");
    }
    else {
        printf("NEITHER");
    }
    return 0;
}