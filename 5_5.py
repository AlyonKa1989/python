# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open('5_5.txt', mode='w+', encoding="utf-8") as f_obj:
    f_obj.write(" ".join([str(randint(1, 50)) for _ in range(15)]))
    f_obj.seek(0)
    print(sum(map(int, f_obj.readline().split())))
