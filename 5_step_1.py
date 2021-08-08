with open("Practic_1.txt", "w") as file_obj:
    str = '0'
    while str != '':
        str = input("Введите новую строку или оставьте поле пустым для окончания записи: ")
        file_obj.write(str + '\n')
