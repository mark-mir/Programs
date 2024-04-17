#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <stdlib.h>

int main()
{
	int money = 100, meal = 10, day_n = 1;
	setlocale(LC_ALL, "RUS");
Day:
	printf("ДЕНЬ %d\n\n", day_n);
	day_n += 1;
	printf("    Ваше положение:\n");
	printf("деньги: %d, еда: %d\n\n", money, meal);
	meal -= 1;
	if (meal <= 3)
	{
		printf("Пора покупать еду...\n");
		money -= 15;
		meal += 5;
		printf("деньги: %d, еда: %d\n\n", money, meal);
	}
	int situation = rand() % 3;
	if (situation == 0)
	{
		printf("Пришло время покупать сезонную одежду\n");
		money -= 50;
		printf("деньги: %d\n\n", money);
	}
	else if (situation == 1)
	{
		printf("К вам заходили гости.\n");
		money -= 20;
		meal -= 4;
		printf("деньги: %d, еда: %d\n\n", money, meal);
	}
	else
	{
		printf("Наконец-то пришла зарплата!\n");
		money += 90;
		printf("деньги: %d\n\n", money);
	}
	_getch();
	goto Day;
}