#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	long long n, m, res;
	scanf("%lld", &n);
	scanf("%lld", &m);
    if (n==1 || n==5) {
        printf("%lld",8*m+(n-1));
        return 0;
    }
    if (m&1) {
        printf("%lld",8*(m/2)+9-n);
    }
    else {
        printf("%lld",8*(m/2)+(n-1));
    }
	return 0;
}