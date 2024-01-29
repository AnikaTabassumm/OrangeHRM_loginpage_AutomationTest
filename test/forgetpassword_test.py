import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.forgetpassword import ForgetPassword


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_forgetpassword(driver):
    forgetPass = ForgetPassword(driver)
    forgetPass.open_loginpage("https://opensource-demo.orangehrmlive.com/")
    forgetPass.click_forgetpassword()
    time.sleep(5)

    assert "requestpasswordresetcode" in driver.current_url.lower(), "Error"
    print("Done")