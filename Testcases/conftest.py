import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):

    driver=webdriver.Chrome()
    wait=WebDriverWait(driver, 10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    #we use this line for other test classes able to reach driver object as well
    request.cls.driver=driver
    request.cls.wait=wait

    #we use yield keyword in pytest for teardown
    yield
    driver.close()


