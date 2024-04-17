#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <string.h>

int main()
{
	setlocale(LC_ALL, ".866");
	//printf("Input text: ");
	char s[5000] = "This is a (simple) text :o) With comments and smiles))) :((( (Comments can be (rather) difficult (with recersion)) :-(";
	char t[5000];
	//scanf_s("%[^\n]s", s, 5000);
	printf("Input text:\n%s\n\n", s);
	int j = 0;
	int counter = 0;
	for (int i = 0; i < strlen(s) + 1; i++)
	{
			if (s[i] == ' ' && s[i+1] == '(')
				counter++;
			if (counter == 0)
                t[j++] = s[i];
			if (s[i] == ')')
				counter--;
	}
	t[j] = 0;
	    printf("Cleaned text:\n%s", t);

	_getch();
}