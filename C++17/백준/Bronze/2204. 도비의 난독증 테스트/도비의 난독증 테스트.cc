#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }

        char ch[21];
        char res[21];
        scanf("%s", res);
        char res2[21];
        for (int i = 0; res[i] != '\0'; i++) {
            res2[i] = toupper(res[i]);
        }
        res2[strlen(res)] = '\0';
        for (int i = 1; i < n; i++) {
            scanf("%s", ch);
            char ch2[21];
            for (int j = 0; ch[j] != '\0'; j++) {
                ch2[j] = toupper(ch[j]);
            }
            ch2[strlen(ch)] = '\0';
            if (strcmp(ch2, res2) < 0) {
                strcpy(res, ch);
                strcpy(res2, ch2);
            }
        }
        printf("%s\n", res);
    }

    return 0;
}
