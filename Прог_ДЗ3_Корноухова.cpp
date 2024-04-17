#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <math.h>

int main()
{
	setlocale(LC_ALL, "RUS");
	double acc, pi_half = 1.0;
	do
	{
		printf("Введите точность: ");
		scanf_s("%lf", &acc);
	} while (acc > 1 || acc <= 0);
	double a = 2.0, b = 1.0;
	int i = 1;
	double t = 0;
	while (fabs(pi_half - t) >= (acc / 2))
	{
		t = pi_half;
		pi_half *= a / b;
		if (i % 2 == 1)
		{
			b += 2;
		}
		else
		{
			a += 2;
		}
		i += 1;
	}
	printf("%lf", pi_half*2);
}