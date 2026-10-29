import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
           self.__name_items.remove(name) 
           self.__number_items -= 1

    def check_amount(self):
        total = []
        for x in self.__name_items:
            total.append(self.__item_price[x])
        if self.__number_items > 10:
            return sum(total) - sum(total) / 10
        else:
            return sum(total)

# В коде лучше умножать или делить когда мы хотим использовать скидку? (просто математически без разницы /10 или *0.1)
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for x in self.__name_items:
            if self.__tax_rate[x] == 20:
                twenty_percent_tax.append(x)
        total = []
        for y in twenty_percent_tax:
           total.append(self.__item_price[y])
        if self.__number_items > 10:
            return sum(total) * 0.2 * 0.9
        else:
            return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for x in self.__name_items:
            if self.__tax_rate[x] == 10:
                ten_percent_tax.append(x)
        total = []
        for y in ten_percent_tax:
            total.append(self.__item_price[y])
        if self.__number_items > 10:
            return sum(total) * 0.1 * 0.9
        else:
            return sum(total) * 0.1    
        
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'


        