class Category:
    """"Этот класс содержит в себе категории продуктов"""
    name: str
    description: str
    __products: list
    total_categories_quantity = 0
    unique_products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories_quantity += 1
        Category.unique_products_quantity += len(products)

    def get_products(self):  # геттер
        """Геттер для получения информации"""
        return [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]

    def get_all_products(self):
        """Геттер для продуктов"""
        return self.__products


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

    def get_price(self):
        """Геттер для получения цены"""
        return self.price

    def set_price(self, new_price):
        """Сеттер для задания новой цены"""
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            if new_price < self.price:
                user_answer = input("Вы хотите снизить цену? 'y' - да, 'n' - нет\n")
                if user_answer == 'y':
                    self.price = new_price
                    print("Операция отменена")
            else:
                self.price = new_price

    @staticmethod
    def make_product(name, description, price, quantity, products_list=None):
        """Метод для создания экземпляров класса Product"""
        if products_list is None:
            return Product(name, description, price, quantity)
        else:
            for product in products_list:
                if product.name == name:
                    new_quantity = int(product.quantity) + quantity
                    new_price = max(price, product.price)
                    return Product(name, description, new_price, new_quantity)
            return Product(name, description, price, quantity)
