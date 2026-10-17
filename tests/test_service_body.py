import pytest
 
from service_body_test import Order
 
 
def make(*pairs):
    """make((100, 2), (50, 1)) -> список товарів з price і quantity"""
    return [{"price": p, "quantity": q} for p, q in pairs]
 
 
# ---------- total() ----------
@pytest.mark.parametrize("items, expected", [
    (make((100, 2), (50, 1)), 250),
    (make((10, 1)), 10),
    ([], 0),
    (make((0, 5), (5, 0)), 0),
    (make((0.1, 3)), pytest.approx(0.3)),
])
def test_total(items, expected):
    assert Order(1, items).total() == expected
 
 
@pytest.mark.parametrize("items, error", [
    (make(("asd", None)), TypeError),
    ([{"price": 10}], KeyError),
    (None, TypeError),
])
def test_total_invalid(items, error):
    with pytest.raises(error):
        Order(1, items).total()
 
 
# ---------- most_expensive() ----------
@pytest.mark.parametrize("items, index", [
    (make((10, 1), (50, 1), (30, 1)), 1),
    (make((99, 1)), 0),
    (make((50, 1), (50, 2)), 0), 
])
def test_most_expensive(items, index):
    assert Order(1, items).most_expensive() is items[index]
 
 
def test_most_expensive_empty():
    with pytest.raises(ValueError):
        Order(1, []).most_expensive()
 
 
@pytest.mark.parametrize("percent, expected", [
    (0, [100, 50]),
    (10, [90, 45]),
    (100, [0, 0]),
])
def test_apply_discount(percent, expected):
    items = make((100, 1), (50, 2))
    Order(1, items).apply_discount(percent)
    assert [i["price"] for i in items] == pytest.approx(expected)
 
 
@pytest.mark.parametrize("percent", [-1, 100.01, 101])
def test_apply_discount_invalid(percent):
    items = make((100, 1))
    with pytest.raises(ValueError):
        Order(1, items).apply_discount(percent)
    assert items[0]["price"] == 100 
 
 
def test_apply_discount_wrong_type():
    with pytest.raises(TypeError):
        Order(1, make((100, 1))).apply_discount("10")
 
 
def test_apply_discount_empty():
    order = Order(1, [])
    order.apply_discount(50)
    assert order.items == []
 
 
# ---------- __repr__() ----------
@pytest.mark.parametrize("items, expected", [
    (make((1, 1), (2, 1)), "<Order 7: 2 items>"),
    ([], "<Order 7: 0 items>"),
])
def test_repr(items, expected):
    assert repr(Order(7, items)) == expected