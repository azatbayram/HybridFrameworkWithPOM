import pytest


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    def test_search_flights(self):

