import pytest
from src.classes import Category, Product, CategoryItems, Smartphone, Grass, Order


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


def test_category_items(test_category):
    test_obj = test_category
    assert (len(list(CategoryItems(test_obj)))) == 3
    new_obj = CategoryItems(test_obj)
    assert next(new_obj).name == 'Samsung Galaxy C23 Ultra'
    assert next(new_obj).name == 'Iphone 15'
    assert next(new_obj).name == 'Xiaomi Redmi Note 11'


@pytest.fixture
def test_some_products():
    grass1 = Grass('t1', '-', 100, 2, 'RUS', 12, 'green')
    grass2 = Grass('t2', '-', 50, 4, 'USA', 20, 'greenest green')
    smartphone1 = Smartphone('t1', '-', 10000, 1, 60, '1', 256, 'green')
    smartphone2 = Smartphone('t1', '-', 20000, 5, 120, '1', 512, 'red')
    obj_list = [grass1, grass2, smartphone1, smartphone2]
    return obj_list


def test_adding_different_products(test_some_products):
    objects = test_some_products
    assert objects[0] + objects[1] == 400  # cкладываем траву с травой =)
    with pytest.raises(TypeError) as exc_info:
        objects[0] + objects[2]  # cкладываем траву со смартфоном xD
    exception_raised = exc_info.type
    assert exception_raised == TypeError


def test_adding_some_prod(product_iphone, category_smartphones):
    assert len(category_smartphones.get_all_products()) == 3
    category_smartphones.add_product(product_iphone)
    assert len(category_smartphones.get_all_products()) == 4
    with pytest.raises(TypeError) as error:
        category_smartphones.add_product('Айфон')  # добавляем в категорию не продукт
    exception_raised = error.type
    assert exception_raised == TypeError
    category_smartphones.add_product(Grass('f', 'f', 1, 1, 'ru', 1, 'rgb'))
    assert len(category_smartphones.get_all_products()) == 5


def test_order(test_some_products):
    item = test_some_products[0]
    order1 = Order(item)
    assert order1.total_price == 200
    assert order1.name == 't1'
    assert order1.quantity == 2


def test_adding_zero_product(product_iphone, category_smartphones):
    """Тестирование добавления товара с количеством = 0"""
    my_cat = category_smartphones
    test_object = product_iphone
    test_object.quantity = 0  # количество товара равно 0
    with pytest.raises(ValueError) as error:
        my_cat.add_product(test_object)  # добавляем продукт в категорию
    test_object.quantity = -1  # количество товара отрицательное
    with pytest.raises(ValueError) as error:
        my_cat.add_product(test_object)  # добавляем продукт в категорию
