#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    int i=1, res=0;
    while (i*i < n) i++;
    int s=i;
    while (i*i <= m) res+=i*i,i++;
    if (res==0) printf("-1\n");
    else printf("%d\n%d",res,s*s);
    return 0;
}