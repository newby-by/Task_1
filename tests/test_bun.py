import pytest

from praktikum.bun import Bun
from data import buns_data


class TestBun:

    @pytest.mark.parametrize(
        'name, price', buns_data
    )
    def test_create_bun_with_expected_data(
        self, name, price
    ):
        actual_bun = Bun(name, price)
        assert (actual_bun.get_name() == name and 
                actual_bun.get_price() == price)
