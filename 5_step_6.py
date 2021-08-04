def gen_dict(pred,sum_hours):
   dict_predmet[pred] = sum_hours

with open('Practic_6.txt', 'r', encoding='utf-8') as file_predmet:
    dict_predmet = {}
    for line in file_predmet:
        predmet = line.split()
        print(predmet)
        sum_hours = 0
        for el in predmet:
            if el.find('(л)') >= 0:
                hours = el.replace('(л)', '')
                sum_hours += int(hours)

            if el.find('(пр)') >= 0:
                hours = el.replace('(пр)', '')
                sum_hours += int(hours)

            if el.find('(лаб)') >= 0:
                hours = el.replace('(лаб)', '')
                sum_hours += int(hours)

            gen_dict(predmet[0], sum_hours)

print(dict_predmet)
