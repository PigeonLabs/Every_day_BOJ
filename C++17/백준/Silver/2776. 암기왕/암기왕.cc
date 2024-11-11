#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int num1 = *(int *)a;
    int num2 = *(int *)b;
    if (num1 < num2)
        return -1;
    else if (num1 > num2)
        return 1;
    else
        return 0;
}

int binsch(int arr[], int len, int key) {
    int l = 0;
    int r = len - 1;
    int m;

    while (l <= r) {
        m = l + (r - l) / 2;
        if (key == arr[m]) {
            return 1;
        } else if (key < arr[m]) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    return 0;
}

int main(void) {
    int n, s1, s2, sn1[1000001], sn2[1000001];

    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%d", &s1);
        for (int i = 0; i < s1; i++) {
            scanf("%d", &sn1[i]);
        }

        qsort(sn1, s1, sizeof(int), compare);

        scanf("%d", &s2);
        for (int i = 0; i < s2; i++) {
            scanf("%d", &sn2[i]);
            if (binsch(sn1, s1, sn2[i])) {
                printf("1\n");
            } else {
                printf("0\n");
            }
        }
    }
    return 0;
}