import pytest
from BestBuy2.src.products import Product, EmptyName, NegativeNumber


def test_creating_prod():
    """
    Test that creating a normal product works.
    All test will pass if all given attributes equal to instance attributes.
    If true then the products have been created successfully.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_creating_prod_invalid_details():
    """
    Test that creating a product with
    invalid details (empty name, negative price) invokes an exception.
    """
    # Empty name test
    with pytest.raises(EmptyName) as exif:
        product = Product("", price=1450, quantity=100)
    assert str(exif.value) == "Product's name cannot be empty.Please enter product name!"

    # Negative price test
    with pytest.raises(NegativeNumber) as exif:
        product = Product("MacBook Air M2", price=-10, quantity=100)
    assert str(exif.value) == "Product's price cannot be below $0.Please enter valid product price!"

    # Negative quantity test
    with pytest.raises(NegativeNumber) as exif:
        product = Product("MacBook Air M2", price=10, quantity=-100)
    assert str(exif.value) == "Product's quantity cannot be below 0.Please enter valid product quantity!"


def test_prod_becomes_inactive():
    """
    This testing function will test if
    when a product reaches 0 quantity, it becomes inactive or not.
    """
    product = Product("MacBook Air M2", price=10, quantity=100)
    product.quantity = 0
    product.set_quantity(product.get_quantity())
    assert product.is_active() == False


def test_buy_modifies_quantity():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    product = Product("MacBook Air M2", price=10, quantity=100)
    product.buy(10)
    assert product.get_quantity() == 90


def test_buy_too_much():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    product = Product("MacBook Air M2", price=10, quantity=100)
    with pytest.raises(NegativeNumber):
        product.buy(101)

