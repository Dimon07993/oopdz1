import pytest
from utils.code import Categoty, Product

@pytest.fixture
def sample_category():
    return Categoty("Test Category", "Category description", [])

@pytest.fixture
def sample_product():
    return Product("Test Product", "Product description", 10.0, 5)

def test_category_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Category description"
    assert sample_category.products == []
    assert sample_category.count_category == 0
    assert sample_category.count_product == 0

def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Product description"
    assert sample_product.price == 10.0
    assert sample_product.count_in_stock == 5

def test_count_category(sample_category):
    sample_category.get_count_category(1)
    assert sample_category.count_category == 1

def test_count_product(sample_category):
    sample_category.get_count_product(1)
    assert sample_category.count_product == 1


if __name__ == "__main__":
    pytest.main()
