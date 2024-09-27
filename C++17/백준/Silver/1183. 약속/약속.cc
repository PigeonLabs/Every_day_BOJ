#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    int a, b, l[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a);
        scanf("%d", &b);
        l[i] = a - b;
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (l[j] > l[j + 1]) {
                int temp = l[j];
                l[j] = l[j + 1];
                l[j + 1] = temp;
            }
        }
    }

    if (n%2) {
        printf("1");
    }
    else {
        printf("%d",abs(l[n/2]-l[n/2-1]+1));
    }

    return 0;
}