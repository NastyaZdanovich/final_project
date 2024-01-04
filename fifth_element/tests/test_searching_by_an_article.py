import allure

from fifth_element.source_code.constants import Info, Host
from fifth_element.source_code.pages.main_page import MainPage
from fifth_element.source_code.pages.search_by_page import SearchPage


class TestClass:
    def test_find_item_by_article(self, driver):
        with allure.step('1. Открыть главную страницу'):
            main_page = MainPage(driver)
            main_page.open(Host.FIFTH_EL)

        with allure.step('2. Заполнить поле поиска товара'):
            main_page.full_in_an_input(Info.ARTICLE)

        with allure.step('3. Нажать кнопку поиска'):
            main_page.click_by_xpath(main_page.search_btn_xpath)

        with allure.step('4. Поиск артикула найденного товара и его проверка'):
            search_page = SearchPage(driver)
            text = search_page.get_a_text(search_page.item_codes_xpath)
            assert text == f"Код товара: {Info.ARTICLE}", f"Expected text: 'Код товара: {Info.ARTICLE}, Actual text: {text}'"
