import products


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        - Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.

        :param shopping_list:
        :return: order_total
        """
        order_total = 0
        for product in shopping_list:
            (name, quantity) = product
            order_total += name.buy(quantity)
            name.set_quantity(name.get_quantity())
        return order_total
