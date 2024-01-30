from source_code.pages.common_page import CommonPage


class MyOZPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.delete_fave_item_xpath = "//*[contains(@class,'product-card__favorite')]"

        self.name_of_an_item_xpath = "//*[@class='product-card__title']"

        self.wait_list_xpath = "//*[contains(@href, 'wait') and @class='personal-nav__link '] "

        self.wait_list_item_xpath = "//*[@class='f12']//*[contains(@href, '/more')]"

        self.delete_wait_list_item = "//*[@class='c-red-d']"

        self.check_wait_list_xpath = "//*[@class='for-editor']//*"

        self.check_wish_list_xpath = "//*[@class='search-info-results__content']//p"
