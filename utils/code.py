import json


class Category():
    name: str
    description: str
    products: list
    count_category = 0
    count_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        # self.count_category = 0
        # self.count_product = 0

    def get_count_category(self, count):
        self.count_category += count

    def get_count_product(self, count):
        self.count_product += count

    def display(self):
        print(f"кол-во категорий {self.count_category}\n"
              f"кол-во продуктов {self.count_product}\n")


class Product():
    name: str
    description: str
    price: float
    count_in_stock: int

    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.count_in_stock = count_in_stock


with open('products.json', encoding='utf-8') as f:
    data = json.load(f)


category = Category(data[0]['name'], data[0]['description'], data[0]['products'])

for category_data in data:
    category.get_count_category(1)
    for product_data in category_data['products']:
        category.get_count_product(1)

category.display()


