#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define max(x, y) (x) > (y) ? (x) : (y)

int n;
int *t,*p;

int solve(int x,int res) {
    if (n<=x) {
        return res;
    }
    if (x+t[x]<=n) {
        return max(solve(x+t[x],res+p[x]),solve(x+1,res));
    }
    else {
        return solve(x+1,res);
    }
}

int main(void) {
    scanf("%d",&n);
    t = malloc(sizeof(int)*n);
    p = malloc(sizeof(int)*n);
    for (int i=0;i<n;i++) {
        scanf("%d %d",&t[i],&p[i]);
    }

    printf("%d",solve(0,0));

    return 0;
}