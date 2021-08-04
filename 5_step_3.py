with open('Practic_3.txt', 'r', encoding="utf-8") as file_zp:
    count = 0
    itog_sum = 0
    for line in file_zp:
        if line != "":
            name_zp, summa_zp_tmp = line.split()
            summa_zp = float(summa_zp_tmp)
            count += 1
            itog_sum += summa_zp
            if summa_zp < 20000:
                print(f"Cотрудник, получающий менее 20000 руб. \n{name_zp}")
print(f"Cредняя зарплата равна:  {itog_sum/count} ")
