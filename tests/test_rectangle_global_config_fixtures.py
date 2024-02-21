import pytest

# This is for the pytest fixtures examples
# here the fixtures are directly fetched from the conftest file


def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(11,13)
    result = my_rectangle.area()
    assert result== (11*13)

# for testing perimeter
def test_perimeter(my_rectangle):
    result = my_rectangle.perimeter()
    assert result == (11**2)+(13**2)


# This is for the pytest mark example
@pytest.mark.slow
def test_diff_area(other_rectangle):
    result = other_rectangle.area()
    assert result == (12*123)

# we can see ..s
@pytest.mark.skip(reason='testing the skip with the same function')
def test_diff_area(other_rectangle):
    result = other_rectangle.area()
    assert False

@pytest.mark.xfail(reason='testing the fail with function')
def test_fail_area(other_rectangle):
    result = other_rectangle.area()
    assert False