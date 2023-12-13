
from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, message: str) -> None:
        self.message = message

    @abstractmethod
    def apply_promotion(self, price, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def apply_promotion(self, price, quantity):
        if quantity >= 2:
            return (price * quantity-1) - (price/2)
        else:
            return quantity * price


class ThirdOneFree(Promotion):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def apply_promotion(self, price, quantity):
        if quantity >= 3:
            return price * (quantity - 1)
        else:
            return quantity * price


class PercentDiscount(Promotion):
    def __init__(self, message: str, percent: int) -> None:
        super().__init__(message)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        return (price-(price * self.percent/100)) * quantity
