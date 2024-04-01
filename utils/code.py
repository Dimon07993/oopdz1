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

    # @property
    # def count(self):
    #     count_product = 0
    #     for i in self.products:
    #         count_product += i['quantity']
    #     return count_product

    def __len__(self):
        count_product = 0
        for i in self.products:
            count_product += i['quantity']
        return count_product


    def __str__(self):
        return f'Название категории: {self.name}, кол-во продуктов: {len(self)} шт.'


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

    def __str__(self):
        return f'Название продукта, {(self.price)} руб. Остаток: {self.count_in_stock} шт.'

    def __add__(self, other):
        return self.price * self.count_in_stock + other.price * other.count_in_stock



with open('products.json', encoding='utf-8') as f:
    data = json.load(f)

category = Category(data[0]['name'], data[0]['description'], data[0]['products'])

for category_data in data:
    category.get_count_category(1)
    for product_data in category_data['products']:
        category.get_count_product(1)

print('----')
category.display()


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

print('----- __str__ Category')

categ_1 = Category("Electronics", "Category for electronic devices", [{'name': 1, 'description': 2, 'price': 3, 'quantity': 4},
                                                                                                {'name': 2, 'description': 3, 'price': 4, 'quantity': 5}])
print(categ_1) #9

print('----- __str__ Product')

prod_1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
print(prod_1)


print('----- __add__ Product')

prod_2 = Product("Smartphone", "Flagship smartphone", 1000.0, 20) #price * count = 20_000
prod_3 = Product("Smartphone_§", "Smartphone", 2000.0, 40) #price * count = 80_000
sum = prod_2 + prod_3
print(sum)


