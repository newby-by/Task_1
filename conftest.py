import random

import pytest

from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture(scope='function')
def database():
    return Database()


@pytest.fixture(scope='function')
def bun(database):
    return random.choice(database.buns)


@pytest.fixture(scope='function')
def ingredient(database):
    return random.choice(database.ingredients)


@pytest.fixture(scope='function')
def burger():
    return Burger()


@pytest.fixture(scope='function')
def burger_with_some_ingredients(burger, database):
    _ = database.ingredients
    ingredients = list(set([random.choice(_) for i in range(len(_))]))
    [burger.add_ingredient(ingredient) for ingredient in ingredients]
    return burger


@pytest.fixture(scope='function')
def burger_with_all_ingredients(burger, database):
    burger.ingredients = database.ingredients
    return burger


@pytest.fixture(scope='function')
def burger_with_some_bun(burger, bun):
    burger.set_buns(bun)
    return burger


@pytest.fixture(scope='function')
def index(burger_with_some_ingredients):
    return random.randint(
        0, len(burger_with_some_ingredients.ingredients) - 1
    )


@pytest.fixture(scope='function')
def indexes(burger_with_all_ingredients):
    numbers = len(burger_with_all_ingredients.ingredients)
    list_numbers = [i for i in range(numbers)]
    index1 = random.choice(list_numbers)
    list_numbers.remove(index1)
    index2 = random.choice(list_numbers)
    return (index1, index2)
