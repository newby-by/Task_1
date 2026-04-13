import pytest

from ingredient import Ingredient
from data import ingredients_data


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price', ingredients_data
    )
    def test_create_bun_with_expected_data(
        self, ingredient_type, name, price
    ):
        actual_ingredient = Ingredient(ingredient_type, name, price)
        assert (actual_ingredient.get_type() == ingredient_type and 
                actual_ingredient.get_name() == name and 
                actual_ingredient.get_price() == price)
