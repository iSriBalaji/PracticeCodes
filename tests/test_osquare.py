import pytest
import source.geo as shapes

# this is for the parameterization example
# it is like you have a clock and wanted to test it with all the batteries you have

# we create one test function and test all the batteries we have

# we can add any no of parameteres and the values should match it
#------------------------ parameters,----------values for parameters-------
@pytest.mark.parametrize("side, expected_area",[(5,25), (4,16), (11,121)] )
def test_multiple_area(side, expected_area):
    assert shapes.Osquare(side).area() == expected_area


@pytest.mark.parametrize("side, expected_area",[(5,50), (4,32), (11,242)] )
def test_multiple_perimeter(side, expected_area):
    assert shapes.Osquare(side).perimeter() == expected_area