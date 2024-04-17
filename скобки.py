# объявление функции
def is_correct_bracket(text):
    counter1 = 0
    for i in range(len(text)):
        if text[i] == '(':
            counter1 += 1
        elif text[i] == ')':
            counter1 -= 1
        if counter1 < 0:
            return False
    if counter1 == 0:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))