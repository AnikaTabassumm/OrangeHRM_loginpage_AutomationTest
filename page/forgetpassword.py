from selenium.webdriver.common.by import By


class ForgetPassword:
    def __init__(self, driver):
        self.driver = driver
        self.forgetPass_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')



    def open_loginpage(self, url):
        self.driver.get(url)


    def click_forgetpassword(self):
        self.driver.find_element(*self.forgetPass_button).click()
