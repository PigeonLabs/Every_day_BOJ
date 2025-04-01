#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n,x,t,res=0;
    scanf("%d",&n);
    int* arr = malloc(sizeof(int)*n);
    for (int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
    }
    x = arr[n-1];
    for (int i=n-2;0<=i;i--) {
        t = arr[i];
        if (x<=t) {
            res += t-x+1;
            t -= t-x+1;
        }
        x = t;
    }
    printf("%d",res);
}