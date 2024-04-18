from utils.Product import *


class Category:
    name: str
    description: str
    products: list
    count_category = 0
    count_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product):
        "Добавление продукта в категорию"
        if not isinstance(product, Product):
            raise TypeError('Операнд должен быть типа Product')

        if product.count_in_stock <= 0:
            raise ValueError('Количество продуктов должно быть положительным числом')

        self.__products.append({'name': product.name, 'description': product.description, 'price': product.price,
                                'quantity': product.count_in_stock})


    @property
    def get_print_price(self):
        return self.__products

    def get_count_category(self, count):
        self.count_category += count

    def get_count_product(self, count):
        self.count_product += count

    def display(self):
        print(f"кол-во категорий {self.count_category}\n"
              f"кол-во продуктов {self.count_product}\n")

    def __len__(self):
        count_product = 0
        for product in self.products:
            count_product += product['quantity']
        return count_product

    def average_price(self):
        "Средняя цена продукта в категории"
        total_price = 0
        for product in self.products:
            total_price += product.price
        if len(self.products) == 0:
            raise ZeroDivisionError
        else:
            return total_price / len(self.products)

    def __str__(self):
        return f'Название категории: {self.name}, кол-во продуктов: {len(self)} шт.'
