# объявление функции
def is_valid_password(password):
    f = password.split(':')
    if len(f) != 3:
        return False
    else:
        if f[0][::] != f[0][::-1]:
            return False
        num = int(f[1])
        if f[1] == 1: # нач второго
            return False
        else: 
            for i in range(2, num):
                if num % i == 0:
                    return False # kon 2
        if int(f[2]) % 2 != 0: # 3
            return False
    return True           

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))