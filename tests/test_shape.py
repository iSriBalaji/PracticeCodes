# good practise to name the file as test_filename
# CLASS based Pytest


# Notes
# class based functions comes with two methods
"""
    1. setup method - run the setup code befiore each test begins
    2. teardown method - tear down the same method
"""

import pytest
import source.geo as shapes


class TestCircle:

    # we wont get all the print statements in the pytest command - for which we need to add -s after pytest to get the print statements
    # pytest -s
    # here we can see two setup and teardown for circle and square
    # we can using this print statements to debug certain tests

    def setup_method(self,method):
        print(f"Setup up the {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"teardown the {method}")
        # for more complicated testing teardown can be useful
        del self.circle


    def test_area(self):
        result = self.circle.area()
        assert result == 314.15

    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 62.83

