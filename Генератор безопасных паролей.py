from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
number_1 = ''
LETTER_1 = ''
letter_1 = ''
symbol_1 = ''
password = ''


print('\nМы рады приветствовать вас в нашем генераторе безопасных паролей!')
print('Надеемся, что он окажется полезным для вас)')
print('Пожалуйста, отвечайте на вопросы символами "+" и "-", а также цифрами\n')


count_pass = input('Укажите количество паролей\n')
while count_pass not in digits:             # защита – работает
   count_pass = input('Пожалуйста, введите цифру\n')
    
len_pass = input('Укажите длину одного пароля\n')
while len_pass not in digits:               # защита – работает
   len_pass = input('Пожалуйста, введите цифру\n')
    
number = input('Включать ли цифры?\n')
while number not in '+-':                   # защита – работает
   number = input('Пожалуйста, отвечайте символом "+", если ваш ответ да, и "-", если нет\n')
if number == '+':
   number_1 += digits
   chars += choice(number_1)
    
LETTER = input('Включать ли прописные буквы?\n')
while LETTER not in '+-':                   # защита – работает
   LETTER = input('Пожалуйста, отвечайте символом "+", если ваш ответ да, и "-", если нет\n')
if LETTER == '+':
   LETTER_1 += uppercase_letters
   chars += choice(LETTER_1)
   #  тут надо чарс += чойс(ЛЕТТЕР_1)
    
letter = input('Включать ли строчные буквы?\n')
while letter not in '+-':                   # защита – работает
   letter = input('Пожалуйста, отвечайте символом "+", если ваш ответ да, и "-", если нет\n')
if letter == '+':
   letter_1 += lowercase_letters
   chars += choice(letter_1)
    
symbol = input('Включать ли символы !#$%&*+-=?@^_?\n')
while symbol not in '+-':                   # защита – работает
   symbol = input('Пожалуйста, отвечайте символом "+", если ваш ответ да, и "-", если нет\n')
if symbol == '+':
   symbol_1 += punctuation
   chars += choice(symbol_1)
   
   
for i in range(int(count_pass)):
   for j in range(int(len_pass)):              
      password += choice(chars)
      print(password) 
#if number or LETTER or letter or symbol != '+' or number or LETTER or letter or symbol != '-':
    #print('Пожалуйста, отвечайте символом "+", если ваш ответ да, и "-", если нет')    # не работает


       