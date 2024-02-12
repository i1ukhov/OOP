import pytest
from src.classes import Category, Product, CategoryItems


@pytest.fixture
def category_smartphones():
    return Category('Smartphones', 'Modern smartphones', ['iPhone XS', 'Samsung Galaxy S123', 'Poco-phone'])


@pytest.fixture
def product_iphone():
    return Product('iPhone XS', 'this is iPhone', 99_999.44, 100)


def test_category_init(category_smartphones):
    assert category_smartphones.name == 'Smartphones'
    assert category_smartphones.description == 'Modern smartphones'
    assert category_smartphones.get_all_products() == ['iPhone XS', 'Samsung Galaxy S123', 'Poco-phone']
    assert Category.total_categories_quantity == 1
    assert Category.unique_products_quantity == 3


def test_get_products(category_smartphones):
    assert category_smartphones.get_all_products() == ['iPhone XS', 'Samsung Galaxy S123', 'Poco-phone']


def test_product_init(product_iphone):
    assert product_iphone.name == 'iPhone XS'
    assert product_iphone.description == 'this is iPhone'
    assert product_iphone.price == 99999.44
    assert product_iphone.quantity == 100


def test_get_price(product_iphone):
    assert product_iphone.get_price == 99999.44


def test_set_price(product_iphone):
    product_iphone.get_price = 100000
    assert product_iphone.get_price == 100000


def test_make_product_just():
    assert Product.make_product('POCO', 'boom', '1000', '1').name == 'POCO'


def test_make_product_additional():
    some_obj_list = [Product('iPhone XS', 'this is iPhone', 99_999.44, 100)]
    assert Product.make_product('iPhone XS', 'blah-blah-blah', 999999, 900, some_obj_list).price == 999999
    assert Product.make_product('iPhone XS', 'blah-blah-blah', 999999, 900, some_obj_list).quantity == 1000


def test_products_addition():
    a = Product('a', '', 100, 10)
    b = Product('b', '', 200, 2)
    assert a + b == 1400


@pytest.fixture
def test_category():
    return Category("Смартфоны", " ",
                    [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                     Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                     Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)])


def test_category_len(test_category):
    assert len(test_category) == 27


def test_callable_func(test_category):
    a = CategoryItems(test_category)
    assert type(a()) == list
    assert len(a()) == 3
