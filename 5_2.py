# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке



with open('5_1.txt', 'r', encoding="utf-8") as f:
    text = [f'В строке №{count} количество слов:  {len(line.split())}. '
            for count, line in enumerate(f, 1)]
    print(*text, f"Количество строк: {len(text)}")

