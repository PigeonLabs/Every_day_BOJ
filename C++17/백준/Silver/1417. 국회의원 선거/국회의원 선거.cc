#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int nums[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    int count = 0;

    while (1) {
        int maxIndex = 1;
        for (int i = 2; i < n; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }

        if (nums[0] > nums[maxIndex]) {
            break;
        }

        nums[maxIndex]--;
        nums[0]++;
        count++;
    }

    printf("%d\n", count);
    return 0;
}