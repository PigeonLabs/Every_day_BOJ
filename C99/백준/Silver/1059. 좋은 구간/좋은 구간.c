#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n,t,r;
    int arr[1001] = { 0 };
    arr[0] = 1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &t);
        arr[t] = 1;
    }
    scanf("%d", &r);
    int left = r, right = r;
    while (!arr[--left]);
    while (!arr[++right]);
    if (arr[r]) printf("0");
    else printf("%d", (r - left) * (right - r) - 1);

    return 0;
}
