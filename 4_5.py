# Реализовать формирование списка, используя функцию range() и
# возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
# randrange(100, 1000, 2) for n in

from random import randrange
from functools import reduce

my_list = [randrange(100, 1000, 2) for n in range(10)]  # 100 и 1000 не попадают в список
my_list.append(1000)
my_list.insert(0, 100)
n_list = list(range(100, 1001, 2))  # слишком длинный список
multiply_m = reduce(lambda x, y: x * y, my_list)

print(f" Список: {my_list}. Gроизведениt всех элементов списка: {multiply_m}")
#print(f"Результат вычисления произведения всех элементов списка: {multiply_n}")
print(f"Список:\n{n_list}\nПроизведениt всех элементов списка:\n{reduce(lambda x, y: x * y, n_list)}")
