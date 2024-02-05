import json
import os
from classes import Category, Product


def read_file():
    """Функция читает json файл"""
    file_path = os.path.join("..", "products.json")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def upload_func():
    """Функция подгружает данные по категориям и товарам, преобразуя данные в экземпляры классов"""
    data = read_file()
    categories_list = []
    products_list = []
    for element in data:
        this_category_products = []
        for product in element['products']:
            name = product['name']
            description = product['description']
            price = product['price']
            quantity = product['quantity']
            new_product = Product(name, description, price, quantity)
            this_category_products.append(new_product)
            products_list.append(new_product)
        cat_name = element['name']
        cat_description = element['description']
        cat_products = this_category_products
        new_category = Category(cat_name, cat_description, cat_products)
        categories_list.append(new_category)
    return categories_list, products_list


print(upload_func())
print(Category.total_categories_quantity)
print(Category.unique_products_quantity)