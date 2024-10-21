#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int main(void) {
    int n;
    int L[21] = {0}, J[21] = {0};
    int dp[101] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &L[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &J[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int health = 99; health >= L[i]; health--) {
            dp[health] = max(dp[health], dp[health - L[i]] + J[i]);
        }
    }

    int maxJoy = 0;
    for (int i = 1; i < 100; i++) {
        if (dp[i] > maxJoy) {
            maxJoy = dp[i];
        }
    }

    printf("%d\n", maxJoy);

    return 0;
}
