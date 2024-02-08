class Category:
    """"Этот класс содержит в себе категории продуктов"""
    name: str
    description: str
    products: list
    total_categories_quantity = 0
    unique_products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories_quantity += 1
        Category.unique_products_quantity += len(products)

    def get_products(self): # геттер
        return [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]


class Product:
    """Этот класс соответствует товарам"""
    name: str
    description: str
    price: int or float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
