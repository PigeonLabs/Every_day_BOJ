#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int E,S,M;
    int e=1,s=1,m=1,res=1;
    scanf("%d %d %d",&E,&S,&M);
    while (E!=e || S!=s || M!=m) {
        e++;s++;m++;res++;
        if (e==16) {
            e = 1;
        }
        if (s==29) {
            s = 1;
        }
        if (m==20) {
            m = 1;
        }
    }
    printf("%d", res);
    return 0;
}