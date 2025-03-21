

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
        return f"{self.name} {self.price} {self.weight}"

    # def menu_from_file(self, filename):
    #     with open("menu.csv", "r") as file:
    #         for line in file:
    #             print(line)


pos1 = MenuItem("coffe", 100, 30)
pos2 = MenuItem("tea", 50, 40)
pos3 = MenuItem("water", 10, 30)
print(pos1, pos2, pos3, sep="\n")




