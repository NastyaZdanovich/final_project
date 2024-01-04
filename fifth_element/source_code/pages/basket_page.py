from fifth_element.source_code.pages.main_page import MainPage


class BasketPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

        # .text возвращает название товра в корзине
        self.item_name_in_a_basket = "//*[@class='c-part']//*[@class='c-text']"
