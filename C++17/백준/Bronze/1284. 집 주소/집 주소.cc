#include <stdio.h>
#include <string.h>

int main() {
    while (1) {
        char n[4];
        scanf("%s", n);
        if (strcmp(n, "0") == 0) {
            break;
        }

        int length = strlen(n);
        int count_1 = 0, count_0 = 0;
        for (int i = 0; i < length; i++) {
            if (n[i] == '1') {
                count_1++;
            } else if (n[i] == '0') {
                count_0++;
            }
        }
        printf("%d\n",count_0*4+count_1*2+(length-count_0-count_1)*3+length+1);
    }
    return 0;
}