#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <stdlib.h>

int main()
{
	int money = 100, meal = 10, day_n = 1;
	setlocale(LC_ALL, "RUS");
Day:
	printf("���� %d\n\n", day_n);
	day_n += 1;
	printf("    ���� ���������:\n");
	printf("������: %d, ���: %d\n\n", money, meal);
	meal -= 1;
	if (meal <= 3)
	{
		printf("���� �������� ���...\n");
		money -= 15;
		meal += 5;
		printf("������: %d, ���: %d\n\n", money, meal);
	}
	int situation = rand() % 3;
	if (situation == 0)
	{
		printf("������ ����� �������� �������� ������\n");
		money -= 50;
		printf("������: %d\n\n", money);
	}
	else if (situation == 1)
	{
		printf("� ��� �������� �����.\n");
		money -= 20;
		meal -= 4;
		printf("������: %d, ���: %d\n\n", money, meal);
	}
	else
	{
		printf("�������-�� ������ ��������!\n");
		money += 90;
		printf("������: %d\n\n", money);
	}
	_getch();
	goto Day;
}