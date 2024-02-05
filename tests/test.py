import pytest
from src.classes import Category, Product


@pytest.fixture
def category_smartphones():
    return Category('Smartphones', 'Modern smartphones', ['iPhone XS', 'Samsung Galaxy S123', 'Poco-phone'])


@pytest.fixture
def product_iphone():
    return Product('iPhone XS', 'this is iPhone', 99_999.44, 100)


def test_category_init(category_smartphones):
    assert category_smartphones.name == 'Smartphones'
    assert category_smartphones.description == 'Modern smartphones'
    assert category_smartphones.products == ['iPhone XS', 'Samsung Galaxy S123', 'Poco-phone']
    assert Category.total_categories_quantity == 1
    assert Category.unique_products_quantity == 3


def test_product_init(product_iphone):
    assert product_iphone.name == 'iPhone XS'
    assert product_iphone.description == 'this is iPhone'
    assert product_iphone.price == 99999.44
    assert product_iphone.quantity == 100
