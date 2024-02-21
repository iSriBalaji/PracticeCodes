import pytest
import source.geo as shapes

# This is for the pytest fixtures examples

# we dont want to repeat certain variables in class based code as we can set it up in the init
# but in functional way of logics we can use pytest fixtures to avoid repeatation of the variables
# we can also make the fictures global that can be used in other places

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(11,13)


def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(11,13)
    result = my_rectangle.area()
    assert result== (11*13)

# for testing perimeter
def test_perimeter(my_rectangle):
    result = my_rectangle.perimeter()
    assert result == (11**2)+(13**2)



