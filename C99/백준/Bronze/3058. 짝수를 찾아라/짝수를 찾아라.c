#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    for(int x=0;x<t;x++) {
        int arr[7];
        int res = 0;
        int mn = 100;
        for (int i=0;i<7;i++) {
            scanf(" %d",&arr[i]);
            if (arr[i]%2==0) {
                res += arr[i];
                mn = arr[i]<mn?arr[i]:mn;
            }
        }
        printf("%d %d\n",res,mn);
    }
    return 0;
}