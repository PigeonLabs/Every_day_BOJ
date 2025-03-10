#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* p1, const void* p2) {
    return (*(int*)p1 - *(int*)p2);
}

int clocknum(int a, int b, int c, int d) {
    int val = 9999;
    int arr[4] = { a, b, c, d };
    for (int i = 0; i < 4; i++) {
        int num = arr[i] * 1000
            + arr[(i + 1) % 4] * 100
            + arr[(i + 2) % 4] * 10
            + arr[(i + 3) % 4];
        if (num < val) val = num;
    }
    return val;
}

int findRank(int t, int clock[], int size) {
    int rank = 1;
    int last = clock[0];
    if (last == t) return rank;
    for (int i = 1; i < size; i++) {
        if (clock[i] != last) {
            rank++;
            last = clock[i];
        }
        if (clock[i] == t) return rank;
    }
    return -1;
}

int main(void) {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int t = clocknum(a, b, c, d);
    static int clockArr[6561];
    int idx = 0;
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= 9; j++) {
            for (int k = 1; k <= 9; k++) {
                for (int l = 1; l <= 9; l++) {
                    clockArr[idx++] = clocknum(i, j, k, l);
                }
            }
        }
    }
    qsort(clockArr, idx, sizeof(int), compare);
    printf("%d\n", findRank(t, clockArr, idx));
    return 0;
}
