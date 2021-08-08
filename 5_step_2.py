with open('Practic_2.txt', 'r', encoding='utf-8') as file_str:
    count = 0
    for line in file_str:
        count += 1
        kol = len(line.split(" "))
        print(f"строка номер  {count} имеет {kol} слов(а)")
    print("Общее количество строк равно: " + str(count))
