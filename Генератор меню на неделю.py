import random

breakfast = ['Мюсли с йогуртом', 'Овсяная каша', 'Творог', 'Кукурузная каша']
main_dish = ['Куриное филе на пару', 'Котлеты на пару', 'Домашние биточки из фарша на пару']
garnish = ['Картофель на пару', 'Брокколи/цветная капуста на пару', 'Макароны', 'Рис', 'Кус-кус']
salad = ['Салат с картофелем и капустой', 'Слоёный салат "Царский"', 'Винегрет', 'Салат "Витаминный"']
weekday = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']

menu = []

for i in range(7):
    print(weekday[i])
    menu.append(random.choice(breakfast))
    menu.append(random.choice(main_dish))
    menu.append(random.choice(garnish))
    menu.append(random.choice(salad))
    print(*menu, sep=', ')
    menu.clear()