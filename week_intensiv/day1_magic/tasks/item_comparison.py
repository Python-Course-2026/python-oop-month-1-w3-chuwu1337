class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""
    def __init__(self, name, price): self.name, self.price = name, price
    def __lt__(self, other): return self.price < other.price
    def __eq__(self, other): return self.price == other.price and self.name == other.name