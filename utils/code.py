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
        self.__products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        name, description, price, quantity = products[0], products[1], products[2], products[3]
        self.__products.append({'name': name, 'description': description, 'price': price, 'quantity': quantity})

    @property
    def get_print_price(self):
        return self.__products
        # for product in self.products:
        #     return f'Продукт, {(product["price"])} руб. Остаток: {product["quantity"]} шт.'

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
        self.__price = price
        self.count_in_stock = count_in_stock

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


with open('products.json', encoding='utf-8') as f:
    data = json.load(f)

category = Category(data[0]['name'], data[0]['description'], data[0]['products'])

for category_data in data:
    category.get_count_category(1)
    for product_data in category_data['products']:
        category.get_count_product(1)

print('----')
category.display()

# str_1 = "999, High-performance laptop, 1500.0, 10"
# str_2 = 'laptop, High-performance laptop, -1500.0, 10'
# str_3 = "laptop, High-performance laptop, 15000.0, 10"
#
# product = Product.new_product(str_1)
# product1 = Product.new_product(str_2)
# product.get_price = str_3

# s1 = product1.format_list
# print(s1, 's1')
# s = product.format_list

# category.products = s1
# category.products = s

category.products = "laptop", "High-performance laptop", 1500.0, 10
print('++++')
print(category.products)
print('----')


s = category.get_print_price
for i in s:
    print(f'{i["name"]}, {(i["price"])} руб. Остаток: {i["quantity"]} шт.')


new_product = Product.new_product('laptop', 'High-performance laptop', 1500.0, 999)
new_product.price = -500
print(new_product.price)

print(new_product.format_list)
