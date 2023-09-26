class Product:
    """
        The 'Product' class represents a specific type of product available in the store (For example, MacBook Air M2).
    It encapsulates information about the product, including its name and price. Additionally, the Product class includes an
    attribute to keep track of the total quantity of items of that product currently available in the store.
    When someone will purchase it, the amount will be modified accordingly.
    """

    def __init__(self, name, price, quantity):
        try:
            while True:
                if name.isspace() or name == "":
                    print("Product's name cannot be empty.Please enter product name!")
                    exit()
                elif price < 0:
                    print("Product's price cannot be below $0.Please enter valid product price!")
                    exit()
                elif quantity < 0:
                    print("Product's quantity cannot be below 0.Please enter valid product quantity!")
                    exit()
                else:
                    self.name = name
                    self.price = price
                    self.quantity = quantity
                    self.active = True
                    break
        except Exception as e:
            print("An error occurred")
            print("Please enter valid name, price and quantity of the product!")

    def get_quantity(self) -> float:
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
        return "{}, Price: {}, Quantity: {}".format(self.name, self.price, self.quantity)

    def buy(self, quantity) -> float:
        total = quantity * self.price
        self.quantity -= quantity
        return total
