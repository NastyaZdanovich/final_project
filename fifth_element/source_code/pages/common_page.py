import time

from fifth_element.source_code.pages.base_page import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



        # xpath инпута для клика
        self.input_xpath_to_click = "//*[@class='h-search']"
        self.cookies_xpath = "//*[text()='Принять']"
        # xpath инпута для заполнения информацией
        self.input_xpath_to_send_keys = "//*[@class='multi-search-header']//input[@type='text']"
        # кнопка поиска
        self.search_btn_xpath = "//*[contains(@class, 'multi-search')]//span[@class='ic-search']"
        # строка с категориями товаров
        self.slider_for_product_categories = "//*[@class='h-panel-nav']//*[contains(@aria-label, '/')]"
        # Иконка '5 элемент'
        self.fifth_element_icon_xpath = "//a[@href='/']"
        # Кпопка 'Cравнение'
        self.comparison_button = "//*[@class='h-bar']//*[contains(@class, 'drop-select')][1]"

    def full_in_an_input(self, value):
        self.click_by_xpath(self.input_xpath_to_click)
        self.fill_in_a_form(self.input_xpath_to_send_keys, value)

    def delay_and_click(self):
        time.sleep(6)
        self.click_by_xpath(self.cookies_xpath)


















