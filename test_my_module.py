# test_my_module.py

import my_module

def test_add():
    assert my_module.add(2, 3) == 5
    assert my_module.add(-1, 1) == 0

def test_subtract():
    assert my_module.subtract(5, 3) == 2
    assert my_module.subtract(1, 1) == 0
