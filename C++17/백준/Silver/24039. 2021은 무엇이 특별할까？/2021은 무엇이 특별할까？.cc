#include <stdio.h>

int main(void) {
    int num[] = {
        6, 15, 35, 77, 143, 221, 323, 437, 667, 899,
        1147, 1517, 1763, 2021, 2491, 3127, 3599, 4087, 4757, 5183,
        5767, 6557, 7387, 8633, 9797, 10403
    };

    int n;
    scanf("%d",&n);
    for (int i = 0; i < sizeof(num)/sizeof(int); i++) {
        if (n < num[i]) {
            printf("%d ", num[i]);
            return 0;
        }
    }
    return 0;
}
