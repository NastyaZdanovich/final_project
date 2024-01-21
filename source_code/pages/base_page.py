import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def assert_element(self, xpath, clickable=False, return_many=False):
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        if clickable:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        if return_many:
            result = driver.find_elements(By.XPATH, xpath)
        else:
            result = driver.find_element(By.XPATH, xpath)

        return result

    def open(self, url):
        self.driver.get(url)

    def click_by_xpath(self, xpath):

        element = self.assert_element(xpath, clickable=True)
        try:
            element.click()
        except Exception:
            element.click()

    def switch_handler(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def fill_in_a_form(self, xpath, value):
        element = self.assert_element(xpath)
        element.send_keys(value)

    def get_a_text(self, xpath):
        element = self.assert_element(xpath)
        text = element.text
        return text

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


    def get_an_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_random_element_by_xpath(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        number_of_elements = len(elements)
        random_index = random.randint(1, number_of_elements)
        random_xpath = f"({xpath})[{random_index}]"
        return random_xpath

    def refresh_page(self):
        self.driver.refresh()
