# 1 2 3 4 5 6 7 8 9 10 11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
#Фибоначче
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

n = int(input('Введите целое число ,больше 1: '))
a1 = 0
a2 = 1
i = 2
while a2 <= n:
    if a2 == n:
        print(i)
        break
    a1, a2 = a2, a1 + a2
    i += 1
else:
    print(-1)
  