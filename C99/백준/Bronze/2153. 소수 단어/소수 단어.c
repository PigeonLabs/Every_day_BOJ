#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>


int main() {
    char str[32];
    scanf("%s", str);
    int len = strlen(str);
    int res = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (97<=str[i] && str[i]<=122) {
            res += str[i] - 96;
        }
        else {
            res += str[i] - 38;
        }
    }
    for (int i = 2; i <= sqrt(res); i++) {
        if (res % i == 0) {
            printf("It is not a prime word.");
            return 0;
        }
    }
    printf("It is a prime word.");
    return 0;
}
