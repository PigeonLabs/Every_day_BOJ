#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int res = 1;
	int i;
	for (i = 1; i <= n; i++) {
		res *= i;
	}
	printf("%d",res);
}