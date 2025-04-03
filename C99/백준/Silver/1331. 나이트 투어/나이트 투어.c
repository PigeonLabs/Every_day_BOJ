#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int visited[6][6] = { 0 };
	char start[6], c1[6], c2[6];
	scanf(" %s", c1);
	strcpy(start, c1);
	visited[c1[0] - 65][c1[1] - 49] = 1;
	for (int i = 1;i < 36;i++) {
		scanf(" %s", c2);
		if (visited[c2[0] - 65][c2[1] - 49] == 1) {
			printf("Invalid");
			return 0;
		}
		visited[c2[0] - 65][c2[1] - 49] = 1;
		if ((abs(c1[0] - c2[0]) == 2 && abs(c1[1] - c2[1]) == 1) ||
			(abs(c1[0] - c2[0]) == 1 && abs(c1[1] - c2[1]) == 2)) {
			strcpy(c1, c2);
		}
		else {
			printf("Invalid");
			return 0;
		}
	}
	strcpy(c2, start);
	if ((abs(c1[0] - c2[0]) == 2 && abs(c1[1] - c2[1]) == 1) ||
		(abs(c1[0] - c2[0]) == 1 && abs(c1[1] - c2[1]) == 2)) {
		printf("Valid");
		return 0;
	}
	printf("Invalid");
	return 0;	
}