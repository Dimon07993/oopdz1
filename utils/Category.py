from utils.Product import Product


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
    def products(self, products):
        """Добавление продуктов в категорию"""
        if not isinstance(products, Product):
            raise TypeError('Операнд должен быть типа Product')
        else:
            name, description, price, quantity = products, products, products, products
            self.__products.append({'name': name, 'description': description, 'price': price, 'quantity': quantity})

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
        try:
            n = 0
            for i in self.products:
                n += i['price']
            print(f'Средняя цена: {n / len(self.products)}')
        except ZeroDivisionError:
            print("0")

    def __str__(self):
        return f'Название категории: {self.name}, кол-во продуктов: {len(self)} шт.'
