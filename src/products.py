# ---Custom Exception Class---
class EmptyName(Exception):
    """
    Raise when product name is empty with no string, space will count as no string.
    """
    pass


class NegativeNumber(Exception):
    """
    Raise when number for price or quantity is below 0. Only use for these two variable only.
    """
    pass


# ---Main Class---
class Product:
    """
        The 'Product' class represents a specific type of product available in the store (For example, MacBook Air M2).
    It encapsulates information about the product, including its name and price. Additionally, the Product class includes an
    attribute to keep track of the total quantity of items of that product currently available in the store.
    When someone will purchase it, the amount will be modified accordingly.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if name.isspace() or name == "":
            raise EmptyName("Product's name cannot be empty.Please enter product name!")
        elif price < 0:
            raise NegativeNumber("Product's price cannot be below $0.Please enter valid product price!")
        elif quantity < 0:
            raise NegativeNumber("Product's quantity cannot be below 0.Please enter valid product quantity!")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactive()

    def is_active(self) -> bool:
        if self.active:
            return True
        return False

    def active(self):
        self.active = True

    def deactive(self):
        self.active = False

    def show(self) -> str:
        return "{}, Price: ${}, Quantity: {}".format(self.name, self.price, self.quantity)

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise NegativeNumber()
        else:
            total = quantity * self.price
            self.quantity -= quantity
            return total
