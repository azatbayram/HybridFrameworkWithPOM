import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    def test_search_flights(self):

        launchPage=LaunchPage(self.driver, self.wait)



