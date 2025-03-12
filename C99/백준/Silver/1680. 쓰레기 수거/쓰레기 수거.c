#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int t;
    scanf("%d",&t);
    for(int x=0;x<t;x++) {
        int w,n,xi,wi;
        int pv=0,q=0,res=0;
        scanf("%d %d",&w,&n);
        for(int i=0;i<n;i++) {
            if (i) pv = xi;
            scanf("%d %d",&xi,&wi);
            res+=xi-pv;
            if (w<q+wi) {
                res+=2*xi;
                q=0;
            }
            q += wi;
            if (w==q && i!=n-1) {
                res+=2*xi;
                q=0;
            }
        }
        res+=xi;
        printf("%d\n",res);
    }
    return 0;
}
