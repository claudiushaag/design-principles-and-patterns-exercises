# TODO: `Product` violates the SRP principle.
#       Identify where the violations occur and discuss/implement
#       a better solution. See exercise_1_hints.py if you need help
from __future__ import annotations
from decimal import Decimal


class Price:
    def __init__(self, price: float|str):
        if isinstance(price, str):
            self._value = Price._price_from_string(price)
        else:
            self._value = price

    def reduced(self, percentage: int) -> None:
        reduced_fraction = Price._price_from_string(str(percentage))/Decimal("100")
        reduction = self._value*reduced_fraction
        reduction = reduction.quantize(Decimal("1.00"))
        self._value = self._value - reduction

    @classmethod
    def _price_from_string(cls, price_str: str) -> Decimal:
        if "." not in price_str:
            return Decimal(f"{price_str}.00")
        elif len(price_str.split(".")[1]) != 2:
            raise IOError("Too many decimal digits")
        return Decimal(price_str)

    def __get__(self, ind) -> float:
        return self._value

    def __str__(self) -> str:
        return f"{self._value}"

class Product:
    def __init__(self, name: str, price: str) -> None:
        self._name = name
        self._price = Price(price)

    def __repr__(self) -> str:
        return f"Product: {self._name}, price: {self._price}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> Decimal:
        return self._price

    def reduced(self, percentage: int) -> Product:
        assert percentage >= 0 and percentage <= 100
        assert not self._is_reduced()
        self._price.reduced(percentage)
        # self._name = f"{self._name} (reduced)"
        return Product(
            name=f"{self._name} (reduced)",
            price=str(self._price)
        )

    def _is_reduced(self) -> bool:
        return "(reduced)" in self._name


if __name__ == "__main__":
    print(Product("Laptop", "999.00"))
    print(Product("Laptop", "999.00").reduced(30))

    a=1
