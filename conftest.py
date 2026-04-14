import pytest

from praktikum.database import Database


@pytest.fixture(scope='function')
def database():
    return Database()
