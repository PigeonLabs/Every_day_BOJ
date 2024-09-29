#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    int p[m];
    for (int i=0;i<m;i++) {
        scanf("%d",&p[i]);
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < (m - 1) - i; j++) {
            if (p[j] > p[j + 1]) {
                int temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }

    int cost,res = 0;
    for (int i = 0; i < m; i++) {
        int egg = (m-i)>n?n:(m-i);
        if (res < p[i]*egg) {
            res = p[i]*egg;
            cost = p[i];
        }
    }

    printf("%d %d",cost,res);

    return 0;
}