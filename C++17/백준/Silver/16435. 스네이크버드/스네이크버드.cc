#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int n,l;
	scanf("%d", &n);
	scanf("%d", &l);
	int h[10000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &h[i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (h[j] > h[i]) {
				int t = h[j];
				h[j] = h[i];
				h[i] = t;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (h[i] <= l) {
			l++;
		}
	}
	printf("%d", l);
	return 0;
}