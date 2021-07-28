def personal_func (fam_pers, god_pers, name_pers, gorod_pers, epost_pers, tel_pers):
    print(f"Имя пользователя - {name_pers}; Фамилия пользователя - {fam_pers}; Год рождения - {god_pers};"
          f" Город - {gorod_pers}; Электронная почта - {epost_pers}; Телефон - {tel_pers}")
personal_func(name_pers = input("Введите свое имя: "), fam_pers = input("Введите свою фамилию: "),
              god_pers = input("Введите год рождения: "), gorod_pers = input("Введите город проживания: "),
              epost_pers = input("Введите e-mail: "), tel_pers = input("Введите телефон: "))