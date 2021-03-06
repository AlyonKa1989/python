#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
#величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
#20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
#сотрудников

#f = open("5_3.txt", "w", encoding="utf-8")
#f.close()

with open('5_3.txt', 'r', encoding="utf-8") as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Оклад менее 20тыс. руб. имеют следующие сотрудники: {[a[0] for a in my_dict.items() if a[1] < 20000]}\n'
          f'Средняя величина дохода сотрудников составляет:{round(sum(my_dict.values()))/len(my_dict), 3}')