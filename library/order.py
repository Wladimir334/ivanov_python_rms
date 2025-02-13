

class Order:
    def __init__(self, order_id, items, total_price, created_at):
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.created_at = created_at

        """
        
        :param order_id: Уникальный идентификатор заказа.
        :param items: Список объектов MenuItem, входящих в заказ.
        :param total_price: Общая стоимость заказа.
        :param created_at: Дата и время создания заказа
        """


        def add_item(self, item: MenuItem):
            pass

        def remove_item(self, item: MenuItem):
            pass