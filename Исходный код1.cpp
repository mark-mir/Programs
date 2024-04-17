#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

const int N = 29, M = 119;
int a[N][M];

void setpixel(int x, int y, int color)
{
	if (x < 0 || x >= M || y < 0 || y >= 2 * N - 2) return;
	if (a[y / 2][x] == 32)
	{
		if (y % 2 == 0)
		{
			if (color == 0)
			a[y / 2][x] = (c == 219) ? 220: 32;
		}
		else
		{
			a[y / 2][x] = (c == 219) ? 220 : 32;
		}
	}
}
int main()
{

	int i, j;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			a[i][j] = 32;
		}
	}
	for (int i = 0; i < 100; i++)
		setpixel(rand() % M, rand() % (2 * N), 1);

	for (i = 0; i < N; i++, printf("\n"))
	{
		for (j = 0; j < M; j++)
		{
			printf("%c", a[i][j]);
		}
	}
	_getch();
}