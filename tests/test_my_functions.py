# note we also names the test modules as test_<module name>
## BASIC TEST

import os
print(os.getcwd())
import pytest
from source.my_functions import add, mul, div, sub


# print(add(5,3))

# testing add with some static test case
# name the test function as test_<function_name>
def test_add():
    result = add(3,4)
    assert result == 7
    ## if the assertion fails it will raise an exception

def test_mul():
    result = mul(5,4)
    assert result == 20

# lets divide by 0 - ZeroDivisionError
def test_div():
    # result = div(123129, 0)
    # assert result == 3421

    with pytest.raises(ZeroDivisionError):  ## we are expecting a ZeroDivisionError from this test
        div(7,0)

# test add function with strings
def test_with_strings():
    result = add('sri ', 'loves to work hard')
    assert result == 'sri loves to work hard'



