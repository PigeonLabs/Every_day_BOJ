#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[101];
    scanf("%s", s);
    for (int i=0; i<strlen(s); i++) {
        if (s[i] == 'C' ||
            s[i] == 'A' ||
            s[i] == 'M' ||
            s[i] == 'B' ||
            s[i] == 'R' ||
            s[i] == 'I' ||
            s[i] == 'D' ||
            s[i] == 'G' ||
            s[i] == 'E') {
            s[i] = '*';
        }
    }
    for (int i=0; i<strlen(s); i++) {
        if (s[i] != '*') {
            printf("%c", s[i]);
        }
    }
    return 0;
}