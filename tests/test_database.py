import data


class TestDataBase:

    def test_database_number_of_buns_is_3(self, database):
        assert len(database.available_buns()) == data.buns_number

    def test_database_number_of_ingredients_is_6(self, database):
        assert (len(database.available_ingredients()) ==
                data.ingredients_number)
