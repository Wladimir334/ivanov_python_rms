

class MenuItem:
    def __init__(self, name, price, weight):
        """
        :param name: имя блюда из меню
        :param price: цена блюда из меню
        :param weight: вес блюда из меню
        """
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} - {self.price} руб, {self.weight} г"

    @staticmethod
    def main():
        menu_items = [
            MenuItem("Кофе", 150.0, 200),
            MenuItem("Чай", 120.0, 180),
            MenuItem("Пицца", 400.0, 600),
            MenuItem("Бургер", 250.0, 300)
    ]
        return menu_items


