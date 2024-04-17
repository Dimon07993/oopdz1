from utils.MixinLog import MixinLog
from utils.ProductTemlate import ProductTemplate


class Product(MixinLog, ProductTemplate):
    name: str
    description: str
    price: float
    count_in_stock: int

    def __init__(self, name, description, price, count_in_stock):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        if count_in_stock > 0:
            self.count_in_stock = count_in_stock
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

    @classmethod
    def new_product(cls, name, description, price, count_in_stock):
        # name, description, price, count_in_stock = name1.split(', ')
        return cls(name, description, price, count_in_stock)

    @property
    def format_list(self):
        return [self.name, self.description, self.__price, self.count_in_stock]

    def get_price(self):
        return self.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        try:
            price = float(new_price)
            if price <= 0:
                print("Пожалуйста, введите корректное значение")
            else:
                self.__price = price
        except ValueError:
            print("Пожалуйста, введите корректное значение")

    def __str__(self):
        return f'Название продукта, {self.price} руб. Остаток: {self.count_in_stock} шт.'

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Операнды должны быть одного типа')
        elif not isinstance(self, other.__class__):
            raise TypeError('Операнды должны быть одного типа')
        else:
            return self.price * self.count_in_stock + other.price * other.count_in_stock

    def full_pra(self):
        return self.price * self.count_in_stock
