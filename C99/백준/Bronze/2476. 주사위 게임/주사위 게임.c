#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int n,a,b,c,res;
    int mx=0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &a, &b, &c);
        if (a==b && b==c) res=10000+a*1000;
        else if (a==b || a==c) res=1000+a*100;
        else if (b==c) res=1000+b*100;
        else res=max(max(a,b),c)*100;
        if (mx<res) mx=res;
    }
    printf("%d", mx);
    return 0;
}
