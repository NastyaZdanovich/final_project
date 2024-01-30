from source_code.pages.common_page import CommonPage


class MainPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_a_category(self):
        category = self.get_random_element_by_xpath(self.catalog_xpath)
        self.click_by_xpath(category)
