#include <stdio.h>
#include <string.h>

int main() {
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int t;
    scanf("%d",&t);
    c += t;
    b += c/60;
    c = c%60;
    a += b/60;
    b = b%60;
    a %= 24;
    printf("%d %d %d\n",a,b,c);
    return 0;
}