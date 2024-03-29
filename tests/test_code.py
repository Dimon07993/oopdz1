import pytest
from utils.code import Category, Product


# Тест для проверки корректности инициализации объектов класса Category
def test_category():
    category = Category("Electronics", "Category for electronic devices", [])
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category.products == []


# Тест для проверки корректности инициализации объектов класса Product
def test_product():
    product = Product("Laptop", "High-performance laptop", 1500.0, 10)
    assert product.name == "Laptop"
    assert product.description == "High-performance laptop"
    assert product.price == 1500.0
    assert product.count_in_stock == 10


# Тест для подсчета количества продуктов
def test_count_products():
    category = Category("Electronics", "Category for electronic devices", [])
    product1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
    product2 = Product("Smartphone", "Flagship smartphone", 1000.0, 20)

    category.products.append(product1)
    category.products.append(product2)

    category.get_count_product(len(category.products))

    assert category.count_product == 2


# Тест для подсчета количества категорий
def test_count_categories():
    categories = []
    categories.append(Category("Electronics", "Category for electronic devices", []))
    categories.append(Category("Clothing", "Category for clothing items", []))

    total_categories = sum(1 for _ in categories)

    for category in categories:
        category.get_count_category(1)

    total_category_count = sum(category.count_category for category in categories)

    assert total_categories == total_category_count


if __name__ == "__main__":
    pytest.main()
