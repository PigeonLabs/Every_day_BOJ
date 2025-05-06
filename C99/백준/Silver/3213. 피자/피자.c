#include <stdio.h>
#include <string.h>

char friend[10001][5] = { 0 };
int main()
{
	int N, i, piece1 = 0, piece2 = 0, piece3 = 0, result = 0, rest = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
		scanf("%s", friend[i]);

	for (i = 0; i < N; i++)
	{
		if (strcmp(friend[i], "1/4")==0)
			piece1++;
		else if (strcmp(friend[i], "1/2")==0)
			piece2++;
		else
			piece3++;
	}
	if (piece2 % 2 == 0)
		result += piece2 / 2;
	else
	{
		result += piece2 / 2;
		rest += 2;
	}

	if (piece1 == piece3)
		result += piece1;
	else if (piece1 > piece3)
	{
		result += piece3;
		rest += piece1 - piece3;
	}
	else if (piece1 < piece3)
	{
		result += piece1 + (piece3 - piece1);
	}

	if (result % 4 == 0)
		result += rest / 4;
	else
		result += rest / 4 + 1;

	printf("%d",result);

	return 0;
}