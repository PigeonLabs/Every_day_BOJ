#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

void multiply(char result[], int number) {
    int carry = 0;
    int len = strlen(result);

    for (int i = len - 1; i >= 0; i--) {
        int current = (result[i] - '0') * number + carry;
        result[i] = (current % 10) + '0';
        carry = current / 10;
    }

    while (carry > 0) {
        int digit = carry % 10;
        carry /= 10;

        for (int i = strlen(result); i >= 0; i--) {
            result[i + 1] = result[i];
        }
        result[0] = digit + '0';
    }
}

int main() {
    while (1) {
        unsigned long long n;
        int res = 0;
        scanf("%llu",&n);
        if (n==0) {
            break;
        }
        else {
            printf("{");
            n--;
            for (int i=0;i<64;i++) {
                if (n%2) {
                    if (res) {
                        printf(",");
                    }
                    char value[1000] = "1";
                    for (int j = 0; j < i; j++) {
                        multiply(value, 3);
                    }
                    printf(" %s", value);
                    res = 1;
                }
                n = n>>1;
            }
            printf(" }\n");
        }
    }
    return 0;
}