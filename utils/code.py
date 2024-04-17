import json
from abc import ABC, abstractmethod

from utils.Category import Category
from utils.LawnGrass import LawnGrass
from utils.Product import Product
from utils.ProductSmartphone import ProductSmartphone



if __name__ == '__main__':
    with open('products.json', encoding='utf-8') as f:
        data = json.load(f)

    category = Category(data[0]['name'], data[0]['description'], data[0]['products'])

    for category_data in data:
        category.get_count_category(1)
        for product_data in category_data['products']:
            category.get_count_product(1)

    print('----')
    category.display()

    # category.products = "laptop", "High-performance laptop", 1500.0, 10
    # print('++++')
    # print(category.products)
    # print('----')

    s = category.get_print_price
    for i in s:
        print(f'{i["name"]}, {(i["price"])} руб. Остаток: {i["quantity"]} шт.')

    new_product = Product.new_product('laptop', 'High-performance laptop', 1500.0, 999)
    new_product.price = -500
    print(new_product.price)

    print(new_product.format_list)

    print('----- __str__ Category')

    categ_1 = Category("Electronics", "Category for electronic devices",
                       [{'name': 1, 'description': 2, 'price': 3, 'quantity': 4},
                        {'name': 2, 'description': 3, 'price': 4, 'quantity': 5}])
    print(categ_1)  # 9

    print('----- __str__ Product')

    prod_1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
    print(prod_1)

    print('----- __add__ Product сложение экземпляров')

    prod_2 = Product("Smartphone", "Flagship smartphone", 1000.0, 20)  # price * count = 20_000
    prod_3 = Product("Smartphone_§", "Smartphone", 2000.0, 40)  # price * count = 80_000
    sum = prod_2 + prod_3
    print(sum)

    print('----- __add__ ProductSmartphone')

    ps = ProductSmartphone("Samsung Galaxy C23 Ultra", "256GB, Серий цвет, 200MP камера", 180000.0,
                           10, 200, "C23", 256, "Серий")
    print(ps)

    print('----- __add__ Нельзя складывать разные экземпляры разных классов TypeError')

    # ps = ProductSmartphone("Samsung Galaxy C23 Ultra", "256GB, Серий цвет, 200MP камера", 180000.0,
    #                         10, 200, "C23", 256, "Серий")
    # prod_4 = Product("Smartphone_§", "Smartphone", 2000.0, 40)
    #
    # # print(prod_4 + ps)
    # print(ps + prod_4)
    # lg = LawnGrass('Green Lawn', 'Beautiful green lawn grass', 20, 100,
    #                'USA', '2 weeks', 'Green')
    #
    # print(ps+lg)

    print('----- Добавление только экземпляра или наследника класса')
    new_product1 = Product.new_product('laptop', 'High-performance laptop', 1500.0, 777)
    print(new_product1)
    print(new_product1.__repr__())

    print('----- full_pra class LagGrass')
    lg1 = LawnGrass('Green Lawn', 'Beautiful green lawn grass', 20, 100,
                    'USA', '2 weeks', 'Green')
    print(lg1.full_pra())

    print('----- MixinLog class ProductSmartphone')

    ps4 = ProductSmartphone("Samsung Galaxy C23 Ultra", "256GB, Серий цвет, 200MP камера", 180000.0,
                            10, 200, "C23", 256, "Серий")
    ps5 = ProductSmartphone("Samsung Galaxy C25", "512GB, Серий цвет, 500MP камера", 280000.0,
                            5, 1000, "C25", 512, "Черный")
    print(ps4.__repr__())
    print(ps5.__repr__())

    # print('----- Ошибка добавления товара с 0 шт.')
    # prod_4 = Product("Smartphone", "Flagship smartphone", 1000.0, 0)

    print('----- Средний ценник категории')
    categ_3 = Category("Electronics", "Category for electronic devices",
                       [{'name': 1, 'description': 2, 'price': 3, 'quantity': 4},
                        {'name': 2, 'description': 3, 'price': 4, 'quantity': 5}])

    categ_3.average_price()

    print('----- Средний ценник категории, ошибка в категории нет товаров вывод 0')
    categ_5 = Category("Electronics", "Category for electronic devices", [])
    categ_5.average_price()
