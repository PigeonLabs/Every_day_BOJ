#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
	int u, n, t, r = -1, res = 99999;
	char name[20];
	char arr[10001][20];
	int price[10001] = { 0 };
	scanf("%d %d", &u, &n);
	for (int i = 0; i < n; i++) {
		scanf("%s %d", &name, &t);
		if (price[t] == 0) {
			strcpy(arr[t], name);
		}
		price[t]++;
	}
	for (int i = 0; i <= u; i++) {
		if (0 < price[i] && price[i] < res) {
			res = price[i];
			r = i;
		}
	}
	printf("%s %d", arr[r], r);
	return 0;
}