#include<stdio.h>
#include<string.h>

int main(void) {

    int num, num1, apb[26] = { 0 };
    char player[150][30] = { 0 };
    int count = 0;

    scanf("%d", &num);

    for (int i = 0; i < num; i++) {
        scanf("%s", player[i]);
    }

    for (int i = 0; i < num; i++) {
        apb[player[i][0] - 97]++;
    }

    for (int i = 0; i < 26; i++) {
        if (apb[i] >= 5) {
            printf("%c", i + 97);
            count++;
        } 
    }
    if (count < 1) {
        printf("PREDAJA");
    }

    return 0;
}