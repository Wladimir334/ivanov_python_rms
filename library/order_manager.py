# from order import Order
import sys
import csv
from menu import MenuItem

class OrderManager:
    # Order.order_list = []
    def __init__(self, source):
        self.library = source



    def main_menu(self):
        print("Добро пожаловать в кафе 'Манговая рулька'")
        print("Выберите нужное действие:")
        print("1. Сделать новый заказ")
        print("2. Показать все заказы")
        print("3. Показать конкретный заказ")
        print("4. Удалить заказ по идентификатору")
        print("5. Сохранить заказ в CSV файл")
        print("6. Загрузить заказ из CSV файла")
        print("7. Показать меню")
        print("0. Выход")

        self.process_main_menu()

    def process_main_menu(self):
        action = input(">>> ")
        match action:
            case "1":
                self.create_order()
            case "2":
                self.view_orders()
            case "3":
                self.view_order()
            case "4":
                self.delete_order()
            case "5":
                self.save_orders_to_csv()
            case "6":
                self.load_orders_from_csv()
            case "7":
                self.menu_from_file()
            case "0":
                sys.exit()
            case _:
                print("Выберите нужный пункт меню")


    def create_order(self):
        print('1')
        self.footer_menu()


    def view_orders(self):
        print('2')
        self.footer_menu()


    def view_order(self):
        print('3')
        self.footer_menu()


    def delete_order(self):
        print('4')
        self.footer_menu()


    def save_orders_to_csv(self):
        print('5')
        self.footer_menu()


    def load_orders_from_csv(self):
        print('6')
        self.footer_menu()

    def menu_from_file(self):
        print('7')
        with open("menu.csv", "r") as file:
            for line in file:
                print(line)
        self.footer_menu()

    def footer_menu(self):
        print("Введите 1 для выхода в главное меню")
        print("Введите 0 для выхода из программы")
        action = input(">>> ")
        match action:
            case "1":
                self.main_menu()
            case "0":
                sys.exit()
            case _:
                print("Выберите необходимое действие")
                self.footer_menu()



    # create_order(): Создает новый заказ.
    # view_orders(): Отображает все заказы.
    # view_order(): Отображает определенный заказ
    # delete_order(order_id: int): Удаляет заказ по его идентификатору.
    # save_orders_to_csv(filename: str): Сохраняет заказы в CSV файл.
    # load_orders_from_csv(filename: str): Загружает заказы из CSV файла.

