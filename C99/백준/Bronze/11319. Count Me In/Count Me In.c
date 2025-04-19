#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) 
        return 0;
    getchar();

    char input[1001];
    for (int i = 0; i < n; i++) {
        if (!fgets(input, sizeof(input), stdin))
            break;

        size_t len = strlen(input);
        if (len > 0 && input[len-1] == '\n')
            input[len-1] = '\0';

        int vow = 0, con = 0;
        for (int j = 0; input[j] != '\0'; j++) {
            switch (input[j]) {
                case 'A': case 'E': case 'I': case 'O': case 'U':
                case 'a': case 'e': case 'i': case 'o': case 'u':
                    vow++;
                    break;
                case ' ':
                    break;
                default:
                    con++;
                    break;
            }
        }

        printf("%d %d\n", con, vow);
    }

    return 0;
}
