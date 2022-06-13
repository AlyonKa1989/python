# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# f = open("5_4.txt", "w", encoding="utf-8")
# f.close()

translator_dict = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
with open("5_4_ru.txt", "w", encoding="utf-8") as new_f:
    with open("5_4.txt", "r", encoding="utf-8") as old_f:
        new_f.writelines([line.replace(line.split()[0], translator_dict.get(line.split()[0])) for line in old_f])

a = open("5_4_ru.txt", "r", encoding="utf-8")
b = [i.strip() for i in a]
print(b)
a.close()
