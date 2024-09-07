#include <stdio.h>
#include <string.h>

int main() {
    for (int i = 0; i < 3; ++i) {
        char n[10];
        fgets(n, sizeof(n), stdin);
        int c = 0;
        for (int j = 0; j < strlen(n); j++) {
            if (n[j] == '0') {
                c++;
            }
        }
        switch (c)
        {
        case 0:
            printf("%s\n","E");
            break;
        case 1:
            printf("%s\n","A");
            break;
        case 2:
            printf("%s\n","B");
            break;
        case 3:
            printf("%s\n","C");
            break;
        case 4:
            printf("%s\n","D");
            break;
        }
    }
    return 0;
}