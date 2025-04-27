#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i = 0;i < n;i++) {
        char line[128];
        fgets(line, 128, stdin);
        for (int x = 0;x < strlen(line);x++) {
            if (65 <= line[x] && line[x] <= 90) {
                line[x] += 32;
            }
            printf("%c", line[x]);
        }
    }
    return 0;
}
