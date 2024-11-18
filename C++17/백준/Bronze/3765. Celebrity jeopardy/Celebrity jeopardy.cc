#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    char res[256];
    while (fgets(res,256,stdin) != NULL) {
        fputs(res,stdout);
    }
    return 0;
}