# ---Custom Exception Class---
import promotions


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


class OverMaximumPurchase(Exception):
    """
    Raise when an order is attempted with quantity larger than the given maximum.
    Mainly use for Limited Product class
    """


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
            self.promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactive()

    def get_promotion(self) -> str:
        return self.promotion.do_promotion()

    def set_promotion(self, promotion):
        self.promotion = promotion

    def is_active(self) -> bool:
        if self.active:
            return True
        return False

    def active(self):
        self.active = True

    def deactive(self):
        self.active = False

    def show(self) -> str:
        if self.promotion is None:
            return "{}, Price: ${}, Quantity: {}, Promotion: {}"\
                .format(self.name, self.price, self.quantity, self.promotion)
        else:
            return "{}, Price: ${}, Quantity: {}, Promotion: {}, Discount" \
                .format(self.name, self.price, self.quantity, self.promotion)

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise NegativeNumber()
        elif self.promotion is not None:
            total = quantity * self.price
            self.quantity -= quantity
            return total
        else:
            total = quantity * self.price
            self.quantity -= quantity
            return total


# ---Sub class---
class NonStockedProduct(Product):
    """
    Some products in the store are not physical, so we don’t need to keep track of their quantity.
    For example - a Microsoft Windows license, McAfee Anti Virus software,...
    On these products, the quantity should be set to zero and always stay that way.
    """

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        super().__init__(name, price, quantity)
        self.default_quantity = quantity

    def show(self) -> str:
        return "{}, Price: ${}".format(self.name, self.price)


class LimitedProduct(Product):
    """
    Some products can only be purchased X times in an order.
    For example - a shipping fee can only be added once.
    If an order is attempted with quantity larger than the maximum one, it should be refused with an exception.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return "{}, Price: ${}, Quantity: {}, Maximum: {} per costumer". \
            format(self.name, self.price, self.quantity, self.maximum)

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise NegativeNumber()
        else:
            total = quantity * self.price
            self.quantity -= quantity
            return total
