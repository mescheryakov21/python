def dict_itog(param_key, param_value):
    dict_temp[param_key] = param_value

with open('Practic_7.txt', 'r', encoding='utf-8') as file_firm:
    # kol_str = len(file_firm.readlines())
    # print(kol_str)
    count = 0
    sum_profit = 0
    exit_list = []
    dict_temp = {}
    dict_average = {}

    for line in file_firm:
        firm_str = line.split()
        # print(firm_str)
        profit = int(firm_str[2]) - int(firm_str[3])
        if profit > 0:
            count += 1
            sum_profit += profit
        dict_itog(firm_str[0], profit)

    averge = sum_profit / count
    dict_average["aver"] = averge
    exit_list.append(dict_temp)
    exit_list.append(dict_average)
    print(exit_list)

    import json
    with open('file_list.json', 'w') as file_json:
        json.dump(exit_list, file_json)


