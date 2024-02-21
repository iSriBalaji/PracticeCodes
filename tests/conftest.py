import pytest

## it is important to name the conftest as file name for the config of pytest

import source.geo as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(11,13)


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(12,123)