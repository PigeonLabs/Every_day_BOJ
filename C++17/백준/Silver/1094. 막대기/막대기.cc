#include <stdio.h>
#include <math.h>

int main() {
	int n;
	int c = 0;
	scanf("%d", &n);
	for (int i=6; i >= 0; i--) {
		int p = (int)(pow(2, i));
		if (n >= p) {
			n -= p;
			c += 1;
		}
	}
	printf("%d", c);
	return 0;
}