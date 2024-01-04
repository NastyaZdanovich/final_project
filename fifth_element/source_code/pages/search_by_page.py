from fifth_element.source_code.pages.main_page import MainPage


class SearchPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

        # .text возвращает строку 'Код товара: ...'
        self.item_codes_xpath = "//*[@class='c-sku']"

        # Список найденных товаров
        self.names_of_items_xpath = "//*[@class='c-part']//*[@class='c-text']"

        # Кнопки 'В корзину' на карточке товаров
        self.add_to_a_basket_button_xpath = "//*[@class='c-controls']//button[@type='button']"

        # Кнопки 'В сравнение' на карточке товара
        self.add_to_compare = "//*[@class='c-actions']//*[@title='В сравнение']"

        # кнопка 'Перейти в корзину' в сплывающем окне после добавление товара в корзину
        self.go_to_a_basket_button_xpath = "//*[@href='/cart' and contains(text(), 'Перейти в корзину')]"






