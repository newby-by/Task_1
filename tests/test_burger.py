class TestBurger:

    def test_set_bun_with_expected_data(self, bun, burger):
        burger.set_buns(bun)
        actual_bun = burger.bun

        assert (actual_bun.get_name() == bun.get_name() and
                actual_bun.get_price() == bun.get_price())

    def test_add_ingredient_with_expected_data(self, ingredient, burger):
        ingredients_number_before = len(burger.ingredients)
        burger.add_ingredient(ingredient)
        ingredients_number_after = len(burger.ingredients)

        assert (ingredients_number_before == ingredients_number_after - 1 and
                burger.ingredients[-1] == ingredient)

    def test_remove_ingredient_with_expected_index(
        self, burger_with_some_ingredients, index
    ):
        burger = burger_with_some_ingredients
        ingredients_number_before = len(burger.ingredients)
        expected_ingredient = burger.ingredients[index]
        burger.remove_ingredient(index)
        ingredients_number_after = len(burger.ingredients)

        assert (ingredients_number_before == ingredients_number_after + 1 and
                expected_ingredient not in burger.ingredients)

    def test_move_ingredient_with_diff_indexes(
        self, burger_with_all_ingredients, indexes
    ):
        burger = burger_with_all_ingredients
        ingredients = burger.ingredients
        index1, index2 = indexes
        ingredient_with_index1 = ingredients[index1]
        ingredients_number_before = len(burger.ingredients)

        burger.move_ingredient(index1, index2)
        ingredient_with_index2 = ingredients[index2]
        ingredients_number_after = len(burger.ingredients)

        assert (ingredient_with_index1 == ingredient_with_index2 and
                ingredients_number_before == ingredients_number_after)

    def test_get_price_burger_with_bun_only(
        self, burger_with_some_bun
    ):
        bun = burger_with_some_bun.bun
        actual_price = burger_with_some_bun.get_price()

        assert actual_price == bun.price * 2
