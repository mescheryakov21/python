def new_file(stroka):
    with open("Practic_4_new.txt", 'a', encoding="utf-8") as file_new:
        file_new.write(stroka)
with open('Practic_4.txt', 'r', encoding="utf-8") as file_num:
    for line in file_num:
        if line.find('One') >= 0:
            line1 = line.replace('One', 'Один')
            new_file(line1)
            continue
        if line.find('Two') >= 0:
            line1 = line.replace('Two', 'Два')
            new_file(line1)
            continue
        if line.find('Three') >= 0:
            line1 = line.replace('Three', 'Три')
            new_file(line1)
            continue
        if line.find('Four') >= 0:
            line1 = line.replace('Four', 'Четыре')
            new_file(line1)
