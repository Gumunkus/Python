""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть """

n = int(input("Введите количество монеток: "))
count_number = 0
count_eagle = 0
for i in range(n):
    count = int(input(f"Введите 0 либо 1 -> "))
    if count == 0:
        count_number += 1
    else:
        count_eagle += 1
if count_number > count_eagle:
    print(f" Необходимо {count_eagle} раз(а) перевернуть орла")
else: 
    print(f" Необходимо {count_number} раз(а) перевернуть решку")