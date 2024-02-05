class Category:
    """"Этот класс содержит в себе категории продуктов"""
    name: str
    description: str
    product: list

    def __init__(self):
        pass


class Product:
    """Этот класс соответствует товарам"""
    name: str
    description: str
    price: int or float
    quantity: int

    def __init__(self):
        pass
