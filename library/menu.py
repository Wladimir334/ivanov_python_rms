

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

    def menu_from_file(self, filename):
        with open("menu.csv", "r") as file:
            for line in file:
                return line





