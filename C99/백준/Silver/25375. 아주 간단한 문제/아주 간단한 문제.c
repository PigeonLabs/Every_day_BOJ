#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
    long long n, a, b;
	scanf("%lld", &n);
    for (long long i = 0;i < n;i++) {
        scanf("%lld %lld", &a, &b);
        if (b % a ==0 && a*2 <= b) {
			printf("1\n");
        }
        else {
            printf("0\n");
        }
    }
	return 0;
}