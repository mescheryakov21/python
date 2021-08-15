class StoreOrgTech: #склад оргтехники
    product_list_itog = []
    def __init__(self):
        # print(self)
        pass

    @staticmethod
    def add_store(dicts):   # "Приход товара на склад"
        if dicts.get('Тип') == "Принтер":
            PrinterOrg("Canon", "Мексика", 2, 13500.0)

        elif dicts.get('Тип') == "Сканер":
            PrinterOrg("Canon", "Ямайка", 1, 4500.0)
        else:
            PrinterOrg("Canon", "Чили", 3, 45700.0)
    def __str__(self):
        for el in self.product_list_itog:
            print(el)

    def del_store(self):    #"Расход товара на склад"
        pass

class OrgTech:
    product_dict = {}
    product_list = ['Принтер', "Сканер", 'Ксерокс']
    def __init__(self, tip, garant = 12): # какой тип продукта, гарантия в месяцах
        self.tip = tip
        self.garant = garant
        if self.product_list.count(tip):
            self.product_dict = {'Тип': self.tip, "Гарантия в месяцах": self.garant}
            # StoreOrgTech.add_store(self.product_dict)
        else:
            print("Данная техника не хранится на этом складе")
        StoreOrgTech.add_store(self.product_dict)


class PrinterOrg(OrgTech):
    def __init__(self, firma, country = 'Россия', count = 0, cent = 1.0): #Фирма,страна, количество, цена
        self.firma = firma
        self.country = country
        self.count = count
        self.cent = cent
        OrgTech.product_dict = {"Фирма": self.firma, "Страна": self.country, "Количество": self.count, "Цена": self.cent}
        StoreOrgTech.product_list_itog.append(OrgTech.product_dict)


class ScannerOrg(OrgTech):
    def __init__(self, firma, country = 'Россия', count = 0, cent = 1.0): #Фирма,страна, количество, цена
        self.firma = firma
        self.country = country
        self.count = count
        self.cent = cent
        OrgTech.product_dict = {"Фирма": self.firma, "Страна": self.country, "Количество": self.count, "Цена": self.cent}
        StoreOrgTech.product_list_itog.append(OrgTech.product_dict)


class XeroxOrg(OrgTech):
    def __init__(self, firma, country = 'Россия', count = 0, cent = 1.0): #Фирма,страна, количество, цена
        self.firma = firma
        self.country = country
        self.count = count
        self.cent = cent
        OrgTech.product_dict = {"Фирма": self.firma, "Страна": self.country, "Количество": self.count, "Цена": self.cent}
        StoreOrgTech.product_list_itog.append(OrgTech.product_dict)

a = OrgTech("Принтер")
print(StoreOrgTech.product_list_itog)

