# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while


i = int(input('Введите целое неотрицательное число: '))
count = 1
pow = 1
while i >= count:
    pow *= count
    count += 1
print(pow)
