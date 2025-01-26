#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int a,b;
    while(scanf("%d %d",&a,&b)!=EOF) {
        int c1 = a-a%b;
        int c2 = a/b+a%b;
        while (b<=c2) {
            c1 += c2-c2%b;
            c2 = c2/b+c2%b;
        }
        printf("%d\n",c1+c2);
    }
}