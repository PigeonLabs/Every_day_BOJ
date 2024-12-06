#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	return (*(int*)a - *(int*)b);
}

int main(void) {
	int n;
	scanf("%d", &n);
	int* arr = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	qsort(arr, n, sizeof(int), compare);

	int res = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] * (n - i) > res) {
			res = arr[i] * (n - i);
		}
	}
	printf("%d", res);
	return 0;
}